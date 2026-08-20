## Description:

Iran Chemical Database is an HTTrack-powered crawler and database application that discovers Iranian chemical suppliers, mirrors supplier sites, extracts research-grade molecule catalog data from local mirrors, validates records with RDKit, PubChem, and CAS checks, and exposes PostgreSQL-backed FastAPI and Streamlit interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and procurement researchers use this skill to deploy and operate a crawler/database that builds a local, searchable reference of research-grade chemical supplier offerings. It supports supplier discovery, mirrored-site parsing, chemical validation, API access, dashboard monitoring, and export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can start privileged local services and an initial web crawl.

Mitigation: Review install.sh before running it, set DB_PASSWORD first, and install only in an isolated environment or trusted network.

Risk: The crawler can make broad outbound requests and supports optional authenticated cookie-based crawling.

Mitigation: Restrict outbound domains to authorized supplier sites and optional public APIs, honor robots.txt and site terms, and do not use cookie-based crawling unless you are authorized to access and archive the target site.

Risk: API and dashboard services can expose collected supplier and molecule data if published without controls.

Mitigation: Keep services on a trusted network by default, add authentication before public exposure, restrict exposed ports, and use TLS at the reverse proxy.

Risk: Extracted supplier, molecule, grade, purity, price, or hazard data can be stale or inaccurate.

Mitigation: Treat the database as a research and procurement reference, verify suppliers and molecules before relying on them, and use RDKit, PubChem, CAS checks, and confidence flags as validation aids rather than final authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [API Reference](docs/api_reference.md)
- [Adding Suppliers](docs/adding_suppliers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, API examples, and code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce deployment steps, crawler configuration, API usage guidance, and code-level implementation assistance for the packaged application.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
