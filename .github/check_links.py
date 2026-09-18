#!/usr/bin/env python3
"""Check that every link in a markdown file still resolves.

The profile README is a page of links to repositories. A repository gets
renamed and the link dies quietly - the visitor sees a 404 on the first thing
they clicked. This is the cheapest possible guard against that.

    python .github/check_links.py README.md

Exits 1 if anything is broken, so it fails the build rather than filing a note
nobody reads. Standard library only.
"""
from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request

LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
UA = "link-check (+https://github.com/dkautomation23)"
TIMEOUT = 20


def status_of(url: str) -> int:
    """HEAD first, GET when HEAD is refused - plenty of servers answer 405."""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if error.code in (403, 405, 501) and method == "HEAD":
                continue
            return error.code
        except Exception:
            return 0
    return 0


def main(paths: list[str]) -> int:
    urls: list[str] = []
    for path in paths:
        with open(path, encoding="utf-8") as handle:
            urls.extend(LINK.findall(handle.read()))

    unique = sorted(set(urls))
    print(f"{len(urls)} link(s), {len(unique)} unique")

    broken: list[tuple[str, int]] = []
    for url in unique:
        code = status_of(url)
        # 429 is the checker being throttled, not the link being broken - the
        # same distinction the rest of these tools make.
        if code == 0 or (code >= 400 and code != 429):
            broken.append((url, code))
            print(f"  BROKEN {code or 'no answer'}  {url}")
        time.sleep(0.2)

    if broken:
        print(f"\n{len(broken)} broken link(s)")
        return 1
    print("\nall links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["README.md"]))
