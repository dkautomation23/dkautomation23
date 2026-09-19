# Security policy

This is the default policy for every repository under
[github.com/dkautomation23](https://github.com/dkautomation23) that does not
carry its own. Most of them do carry their own, because what counts as a
vulnerability differs from tool to tool; that file wins where it exists.

## Reporting

Use GitHub's private reporting on the repository in question:
**Security → Report a vulnerability**. It creates a private thread with me and
nothing is public until there is a fix.

If that is not available to you, write to **hello@dkautomation.dev** with the
repository name in the subject.

Please include the version, the exact command or request, and what happened.
A proof of concept is welcome; a scanner's raw output usually is not.

**Do not open a public issue for a vulnerability.** A public issue is a
disclosure, and it is unfair to anyone running the tool.

## What to expect

| | |
|---|---|
| First reply | within 2 working days |
| Assessment | within 7 working days of the first reply |
| Fix or a stated decision not to fix | within 30 days for anything I can reproduce |

These are a single person's commitments, not a company SLA, and they are what I
have kept so far rather than what sounds impressive.

## Scope

Supported: the latest release of each tool, and the default branch.

In scope, in general terms:

- input from outside the operator — a file, a webhook, an API response, a page
  fetched from a third party — that causes the tool to read or write somewhere
  it was not asked to, execute code, or send data to an unintended place;
- a secret ending up somewhere it should not: a log, a report, a saved
  baseline, a committed fixture;
- a check that reports "clean" for something it did detect, where the tool's
  job is exactly to report it.

Out of scope:

- a missed finding in a detection tool. That is a bug — open an issue, it will
  be taken seriously, but it is not a vulnerability;
- anything requiring the operator to run the tool against their own machine on
  purpose, with the flags that say so;
- the availability of a third-party service the tool reads from;
- findings from an automated scanner with no demonstrated impact.

## Credit

If you want it, you are named in the release notes for the fix. If you prefer
not to be, say so and you will not be.

There is no bug bounty. I am one person and I would rather promise nothing than
promise money I have not set aside.
