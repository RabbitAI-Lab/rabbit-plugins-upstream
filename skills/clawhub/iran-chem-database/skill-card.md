## Description:

Iran Chemical Database helps agents install and operate a best-effort crawler and database for public Iranian chemical supplier catalogues, with local mirroring, validated molecule extraction, coverage reporting, and export workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, researchers, and procurement analysts use this skill to set up a local crawler-backed chemical catalogue database, query public supplier listings, and export auditable molecule or offering records with coverage context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer and service startup can execute local deployment steps and expose database, cache, API, or dashboard services if run without review.

Mitigation: Install in an isolated, trusted environment; review install.sh and .env first; bind PostgreSQL and Redis to localhost or the Compose network; add authentication and TLS before exposing API or dashboard services.

Risk: Crawler configuration allows broad outbound network access to supplier sites and optional public APIs.

Mitigation: Allowlist only intended supplier domains and required validation or search APIs, keep polite rate limits enabled, and verify that mirroring is authorized for each target site.

Risk: Optional AI normalization can send crawled listing text to configured external providers.

Mitigation: Disable or explicitly verify ICDB_ROUTER and AI provider settings before processing sensitive sources, and rely on PubChem confirmation rather than unverified generated identities.

Risk: Chemical catalogue data can be incomplete, stale, or misleading if coverage and export manifests are ignored.

Mitigation: Check coverage endpoints and export manifests before relying on results; present the database as a dated best-effort supplier-offering index, not complete market coverage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [Coverage Report](data/seed_export/coverage_report.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code references, configuration guidance, and API usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state crawl coverage before presenting database results and distinguish confirmed organic records from unknown-organic records.]

## Skill Version(s):

2.22.11 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
