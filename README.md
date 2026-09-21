## Dmytro Galko

I measure what AI systems actually do, and build the unglamorous tooling that
keeps them honest: evals with a control group, red-teaming of what an agent
reads, multi-provider LLM pipelines that fail loudly instead of quietly, and the
audits that catch a silent change before a customer does.

Every repository below runs on a clean machine with one command, has its own
tests in CI, and documents what it deliberately does **not** do. Where a README
claims a number, the script that produced it is in the repository — and where a
number turned out to be wrong, the correction is in the git history rather than
quietly overwritten.

### AI and agents

| Repo | What it does |
| --- | --- |
| [model-eol](https://github.com/dkautomation23/model-eol) | On 23 October 2026 OpenAI retires eighteen model identifiers in one day, five days after four more go on 28 September. GitHub code search puts 96,640 files on `gpt-4-0613` alone and 86,528 on `gpt-4-turbo` in Python - each a hardcoded string that starts failing on a published date with no warning first. This answers what comes before "how do I migrate": what of mine dies, when, and what replaces it. One run, no key, exit 1 for CI. A retired id is a prefix of live ones, so matching is bounded and longest-first, and the suite asserts that none of ten live look-alikes is ever reported. |
| [agent-hijack-bench](https://github.com/dkautomation23/agent-hijack-bench) | How often does a model used as an agent obey an instruction planted in a file a website publishes *for it to read*? Nineteen local models, temperature 0, scored by canary substring so no judge model is involved, with a control case that voids a model's numbers if it emits the canary unprompted. Six models refuse everything and two fall for three families out of four. The data-exfiltration framing beats twelve of the thirteen hijackable models every single time, the blunt "SYSTEM OVERRIDE" spoof works on exactly one, parameter count predicts nothing, and a published mitigation helps ten models while making two measurably worse. Runs offline on Ollama. |
| [embed-drift](https://github.com/dkautomation23/embed-drift) | When a provider swaps the embedding model under a live vector index, nothing raises an error - the nearest neighbours are simply wrong from then on, and the blame lands on the language model rather than the retrieval step. Pins a fingerprint of twelve frozen probes and reports two numbers: vector drift catches any change including a harmless renormalisation, while drift in the geometry between probes only moves when retrieval will actually return different rows. A baseline on all-minilm against a different model of the same 384 dimensions collapses the first number to -0.0052 and the second to 0.349. |
| [llm-doc-extractor](https://github.com/dkautomation23/llm-doc-extractor) | Documents to schema-shaped JSON across Anthropic, OpenAI and local Ollama behind one schema. The part that matters is what happens when a model returns something that does not fit: it is caught, reported and retried against the declared shape rather than written downstream. |

### Upstream contributions

- **[mozilla/bedrock#17391](https://github.com/mozilla/bedrock/pull/17391)** — mozilla.org's
  `security.txt` used field names that predate RFC 9116, so a conforming parser
  found no `Contact` and no `Expires` and treated the file as invalid: automated
  vulnerability reporting could not find where to report a bug in a Mozilla
  property. Found with my own `well-known-audit`, fixed, reviewed and approved by
  Mozilla's security team.
- **[jupyter/jupyter.github.io#887](https://github.com/jupyter/jupyter.github.io/pull/887)** —
  the same audit, the missing mandatory `Expires` field.
- **[Universal-Commerce-Protocol/ucp#840](https://github.com/Universal-Commerce-Protocol/ucp/pull/840)** —
  the spec's own example validator crashed on a UTF-8 file and on a missing
  binary; fixed with a clear failure message instead of a traceback. Merged by
  Google and Shopify's UCP maintainers on 21 September 2026.

### Open data

**[One in ten sites that publish a guide for AI also ban the readers](https://dkautomation23.github.io/llms-txt-conformance.html)** —
Tranco top 1,500, 19 September 2026. How many sites publish an `llms.txt` has
been counted several times this year; nobody had asked whether the files work.
Of the 123 that exist, 13 belong to sites whose `robots.txt` bans by name a
crawler that would read them, and 13.5% point at least one link at a page that
is gone. Unreachable hosts, hosts that refused, and hosts answering 200 to a
path that cannot exist are each counted separately and kept out of every rate.
Raw CSV, domain list and both scripts in
[well-known-audit/survey](https://github.com/dkautomation23/well-known-audit/tree/main/survey).

**[Half the security.txt files at the top of the web are invalid](https://dkautomation23.github.io/security-txt-survey.html)** —
500 most visited sites, 18 September 2026. A `security.txt` tells a researcher
where to report a hole; RFC 9116 makes its `Expires` field mandatory and treats
an expired file as no file at all. Of the 158 that exist, 92 have no `Expires`
and 6 have expired — 62% are not valid, and nothing anywhere warns when that
happens. Raw results in
[well-known-audit/survey](https://github.com/dkautomation23/well-known-audit/tree/main/survey).

**[What AI shopping agents actually see](https://dkautomation23.github.io/ucp-survey.html)** —
a census of 5,356 live Shopify storefronts, 18 September 2026. Google and Shopify
published the Universal Commerce Protocol so an agent can read a shop and buy from
it; nobody had published a count of how many shops actually speak it. 98.9% do, all
on the current release, none with a blocker — and 47.5% will not let an agent sign
the shopper into their own account, which turns a returning customer into an
anonymous visitor. The domain list, both scripts and the raw per-domain results are
in [ucp-audit/survey](https://github.com/dkautomation23/ucp-audit/tree/main/survey),
so the measurement can be repeated rather than believed.

### Command-line tools — Rust

| Repo | What it does |
| --- | --- |
| [csvdiff](https://github.com/dkautomation23/csvdiff) | Diffs two CSV exports by key. 2M rows in 2.8s, per-column change breakdown, number/null normalisation so a migration report is readable instead of 995 000 rows of noise. Benchmark script included. |
| [leakscan](https://github.com/dkautomation23/leakscan) | Offline check of what leaves with a file: tracked changes with the deleted text still readable, hidden worksheets, PDF attachments, GPS in photos, validated card/IBAN data. |
| [imgdupe](https://github.com/dkautomation23/imgdupe) | Perceptual-hash duplicate finder. Complete-linkage grouping so unrelated pictures never chain together; writes a delete script instead of deleting. |
| [linkscan](https://github.com/dkautomation23/linkscan) | Crawls a site and reports the links that are genuinely broken, keeping bot protection and timeouts out of the "broken" column. |

### Integration tooling — TypeScript

| Repo | What it does |
| --- | --- |
| [webhook-rewind](https://github.com/dkautomation23/webhook-rewind) | Record the webhooks a provider sends you once, then replay them at your own code — re-signed for Meta, GitHub, Shopify or Stripe, so the receiver runs its real verification instead of having it switched off for the debugging session. |
| [well-known-audit](https://github.com/dkautomation23/well-known-audit) | A site publishes a dozen small files at its root — `security.txt`, `robots.txt`, `llms.txt`, `assetlinks.json`, `mta-sts.txt` — each checked by a different tool or by nobody. This reads all of them in one run and says which are missing, malformed, or quietly expired: RFC 9116 gives `security.txt` an `Expires` date, and past it the file is no longer valid. |
| [ucp-audit](https://github.com/dkautomation23/ucp-audit) | Google and Shopify's Universal Commerce Protocol lets AI agents shop: every business publishes a profile at `/.well-known/ucp` and agents read it to decide what they can do. The failure mode is silence — offer checkout without declaring a searchable catalogue and no agent ever surfaces your products. This reads the profile the way an agent does and says what one would conclude. |
| [cra-report](https://github.com/dkautomation23/cra-report) | Since 11 September 2026 a manufacturer placing a product on the EU market has 24 hours to notify ENISA of an *actively exploited* vulnerability in it. This joins OSV with the CISA KEV catalogue to say which of a hundred advisories actually starts that clock, and drafts the Article 14 notification for the ones that do. |
| [api-drift](https://github.com/dkautomation23/api-drift) | Records the shape of a JSON API and reports when it changes: removed fields, changed types, values that can now be null. Exits non-zero in CI, so a partner's silent rename stops being something you find out about two weeks later. |

### Business automation — Python

| Repo | What it does |
| --- | --- |
| [invoice-reconciler](https://github.com/dkautomation23/invoice-reconciler) | Matches a bank statement against open invoices in five passes — references, part payments, batch transfers, instalments — and reports only what does not add up. Standard library only. |
| [lead-responder](https://github.com/dkautomation23/lead-responder) | Answers a web enquiry in under a second: scores it, writes a personal reply, offers real call slots, escalates the hot ones, files the spam. Rules in YAML, no API keys. |
| [email-deliverability-check](https://github.com/dkautomation23/email-deliverability-check) | Finds why a domain's mail lands in spam: SPF lookup limit, duplicated records, revoked DKIM keys, DMARC stuck at `p=none`, missing MTA-STS. DNS only, batch mode for client lists. |
| [shopify-catalog-auditor](https://github.com/dkautomation23/shopify-catalog-auditor) | Audits any Shopify store's public catalogue for the gaps that cost sales. No API keys or store access needed. |
| [ai-visibility-audit](https://github.com/dkautomation23/ai-visibility-audit) | Checks whether AI assistants can actually read a site: crawler access for ten named agents, JS dependence, structured data, trust signals. |
| [price-stock-monitor](https://github.com/dkautomation23/price-stock-monitor) | Config-driven price and restock monitor with SQLite history and webhook alerts. |

### Integrations and pipelines

| Repo | What it does |
| --- | --- |
| [whatsapp-crm-connector](https://github.com/dkautomation23/whatsapp-crm-connector) | WhatsApp Business Cloud webhooks into a CRM: signature verification, instant ACK plus queue, de-duplication, conversations logged against both contact and company, 24-hour window, token refresh. |
| [instagram-metrics-reader](https://github.com/dkautomation23/instagram-metrics-reader) | Read-only Instagram Business metrics over the Meta Graph API, with read-only scopes enforced in code, caching against rate limits and stale-data flagging. |
| [mcp-data-server](https://github.com/dkautomation23/mcp-data-server) | An MCP server giving an assistant read-only access to a business database: table allowlist, PII masking, row caps, query timeout, full audit log. |
| [llm-doc-extractor](https://github.com/dkautomation23/llm-doc-extractor) | Schema-driven document to structured JSON, with a no-API-key demo mode so the pipeline can be watched end to end before any keys exist. |
| [automation-pipelines](https://github.com/dkautomation23/automation-pipelines) · [web-scraper-toolkit](https://github.com/dkautomation23/web-scraper-toolkit) | Webhook intake, cleaning and scoring into Google Sheets; a polite scraper with retries, backoff and de-duplication. |

### n8n

| Repo | What it does |
| --- | --- |
| [n8n-workflow-reliability-kit](https://github.com/dkautomation23/n8n-workflow-reliability-kit) | Error intake, heartbeat monitoring and a smoke test for n8n workflows already in production. |
| [n8n-workflow-templates](https://github.com/dkautomation23/n8n-workflow-templates) | Importable templates built to the n8n Creator Portal conventions, validated in CI against leaked credentials and broken exports. |

### Developer tooling

| Repo | What it does |
| --- | --- |
| [repo-secret-scanner](https://github.com/dkautomation23/repo-secret-scanner) | Dependency-free leaked-secret scanner for pre-commit and CI: API keys, tokens, private keys, JWTs plus an entropy check. Redacted output, non-zero exit on a hit. |

### Working with

Python · Rust · TypeScript/Node · FastAPI · SQLite/PostgreSQL · n8n ·
Meta Graph API · Shopify · Google Sheets · GitHub Actions · Docker

### Work with me

The tools above exist because the same problems keep arriving. If one of them
sounds like your week, I take on the work behind it:

- **Something breaks and nobody notices.** A workflow that stopped running, an
  API that changed shape, a feed that has been half-empty for a fortnight —
  monitoring that names the failure instead of a dashboard nobody opens.
- **Two systems that will not agree.** Webhooks into a CRM, a bank statement
  against invoices, a catalogue against a supplier feed. Signature verification,
  de-duplication, retries and the 3am cases, not the happy path.
- **Data that has to be right.** Migration checks, reconciliation, audits of a
  catalogue, a domain's mail or a site's crawlability, with the numbers
  reproducible rather than asserted.
- **Rescue work.** An automation someone else built and left. I will read it and
  tell you honestly whether it is worth repairing.

**hello@dkautomation.dev** — tell me what breaks today and what it costs you.
You get back an approach and a number, or an honest "this is not my job" and who
to ask instead. Based in Bulgaria, working with clients across the EU, UK and US.

More at [dkautomation23.github.io](https://dkautomation23.github.io) ·
[security policy](https://github.com/dkautomation23/.github/blob/main/.github/SECURITY.md) ·
everything MIT licensed.
