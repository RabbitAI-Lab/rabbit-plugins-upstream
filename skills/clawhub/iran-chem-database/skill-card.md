## Description:

Iran Chemical Database builds a live, dated, auditable best-effort index of chemical offerings in configured public Iranian supplier catalogues and public Telegram channels, using local mirroring, chemical identity validation, PostgreSQL, FastAPI, and Streamlit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External developers and research teams use this skill to deploy and query a best-effort chemical catalogue index for configured Iranian supplier sources. It supports crawling, local parsing, identity validation, coverage reporting, and export workflows while preserving source and coverage caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation starts persistent local services and exposes API, dashboard, database, cache, and nginx ports if deployed without network controls.

Mitigation: Run on an isolated host or container environment, restrict ports 80, 8501, 5432, and 6379 to localhost or a VPN, and add authentication before exposing the API or dashboard.

Risk: The skill performs broad outbound crawling of configured supplier sources and optional lookups through PubChem, search APIs, Telegram previews, and AI providers.

Mitigation: Disable free-access fallbacks, search keys, Telegram crawling, or AI provider keys when those external calls are not desired, and review configured supplier targets before starting crawls.

Risk: Mirrored public-web catalogue data can be stale, incomplete, legally constrained, or mistaken for stock availability or a national market census.

Mitigation: Check coverage endpoints and export manifests, preserve best-effort and listing-not-stock caveats, and verify suppliers and molecules before relying on results.

Risk: Weak or placeholder deployment secrets can expose database-backed services.

Mitigation: Set a strong DB_PASSWORD through the environment or .env file before deployment and avoid exposing local service ports directly to untrusted networks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [Coverage Report](data/seed_export/coverage_report.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, API query examples, configuration notes, and file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CSV, JSON manifest, SQLite, and database-backed API outputs when the installed services or included seed tools are run.]

## Skill Version(s):

2.22.0 (source: frontmatter and release evidence, released 2026-08-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
