## Description:

Iran Chem Database helps agents inspect, mirror, parse, validate, and report on configured public Iranian chemical supplier catalogues as a dated, auditable, best-effort chemical-offering index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, researchers, and analysts use this skill to run or query a local crawler/database workflow for public supplier catalogue evidence, seed exports, molecule identity checks, coverage status, and audit-ready reports. It is intended to support academic procurement research and requires users to verify supplier, coverage, and molecule claims before relying on results.

### Deployment Geography for Use:

Global use; data scope is limited to configured public Iranian supplier catalogues.

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the crawler/database application exposes broad deployment and URL-handling attack surface.

Mitigation: Install only in an isolated or trusted network, restrict crawler egress to approved public domains, and review the skill before installation.

Risk: PostgreSQL, Redis, Streamlit, nginx, API, and dashboard services may be exposed by an unsafe deployment.

Mitigation: Bind services to localhost or an internal network and add authentication before production use.

Risk: Optional AI normalization may route crawled listing text to configured AI providers.

Mitigation: Disable or explicitly verify AI router paths when source listings are sensitive, and independently confirm normalized identities.

Risk: Shipped seed data and crawled catalogue entries can be incomplete, stale, or unsuitable as procurement proof.

Mitigation: Treat seed data as a starting point, check coverage endpoints or manifests, and verify every supplier and molecule before relying on results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [Adding Suppliers](docs/adding_suppliers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API examples, configuration notes, and references to generated files or exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state coverage status, row counts, provenance hashes or manifests when relevant, and limits such as catalogue evidence not proving stock or market completeness.]

## Skill Version(s):

2.22.12 (source: ClawHub release evidence; artifact frontmatter reports 2.22.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
