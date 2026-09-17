## Dmytro Galko

I build the unglamorous tools that businesses run every day: data reconciliation,
catalogue and deliverability audits, webhook-to-CRM integrations, and the
monitoring that tells you an automation stopped working before a customer does.

Every repository below runs on a clean machine with one command, has its own
tests in CI, and documents what it deliberately does **not** do. Where a README
claims a number, the script that produced it is in the repository.

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
| [webhook-replay](https://github.com/dkautomation23/webhook-replay) | Record the webhooks a provider sends you once, then replay them at your own code — re-signed for Meta, GitHub, Shopify or Stripe, so the receiver runs its real verification instead of having it switched off for the debugging session. |
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

Based in Bulgaria, working with clients across the EU, UK and US.
Open an issue on any repository, or reach me through my GitHub profile.
