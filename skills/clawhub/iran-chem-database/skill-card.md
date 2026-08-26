## Description:

Iran Chemical Database indexes configured public Iranian supplier catalogues and public Telegram channels as a dated, auditable, best-effort research-grade chemical offering database with local parsing, RDKit/PubChem/CAS validation, FastAPI, and Streamlit access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and procurement analysts use this skill to deploy and query a crawler-backed database of configured Iranian research-grade chemical supplier offerings. Agents should check crawl coverage and export manifests before presenting molecule or supplier results as reliable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package runs persistent local services, including database, queue, API, dashboard, reverse proxy, workers, and scheduled crawls.

Mitigation: Install it only on infrastructure intended for these services, keep API and dashboard endpoints on a trusted network, and add authentication before exposing them.

Risk: The crawler can generate broad outbound traffic to configured supplier sites, Telegram previews, archive or proxy services, PubChem, search providers, and optional AI providers.

Mitigation: Review configured suppliers and relay settings, use polite crawling defaults, and restrict egress to approved destinations when operating in a controlled environment.

Risk: Weak or placeholder database credentials can expose the local PostgreSQL service.

Mitigation: Set a strong DB_PASSWORD before install and manage secrets through the environment or .env file.

Risk: Optional AI normalization may send crawled listing text to configured AI providers.

Mitigation: Review AI provider settings before enabling that path and disable it when source listing text is sensitive.

Risk: Supplier and molecule records are best-effort catalogue observations, not verified stock or complete market coverage.

Mitigation: Check coverage endpoints and export manifests, preserve row counts and provenance hashes, and verify supplier and molecule records before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [HTTrack Integration](docs/httrack_integration.md)
- [Release changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API examples, configuration steps, and structured export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference CSV, JSON, SDF, manifest, SQLite, and database outputs produced by the installed application.]

## Skill Version(s):

2.21.1 (source: SKILL.md frontmatter, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
