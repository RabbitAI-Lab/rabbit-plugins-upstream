## Description:

Iran Chemical Database is an HTTrack-powered live crawling system that builds a dated, auditable, best-effort index of confirmed and unresolved chemical offerings discovered in configured public Iranian supplier catalogues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, lab managers, procurement staff, and developers use this skill to deploy and operate a searchable supplier-offering index for Iranian chemical catalogues. Agents can use it to configure crawling, inspect coverage, export auditable molecule or offering data, and explain unresolved records without claiming complete market coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill starts persistent networked services and automated web crawling, which require review before installation.

Mitigation: Install only in a contained trusted environment, review the supplier list and crawl schedule before starting workers, and keep Redis, the API, and the dashboard off public interfaces or add authentication.

Risk: Broad outbound crawling can reach arbitrary configured supplier sites.

Mitigation: Use egress allowlisting where possible and avoid cookie-based crawling unless explicit authorization exists.

Risk: Production use can inherit dependency and service hardening gaps.

Mitigation: Pin dependencies for production deployments and apply the documented service-hardening guidance before exposing the system.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Architecture](docs/architecture.md)
- [API reference](docs/api_reference.md)
- [Deployment guide](docs/deployment_guide.md)
- [HTTrack integration guide](docs/httrack_integration.md)

## Skill Output:

**Output Type(s):** [code, shell commands, configuration, markdown, guidance]

**Output Format:** [Markdown guidance with bash examples, configuration files, Python application code, Docker Compose files, API responses, and CSV or JSON exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation provides software and queued jobs, not a populated dataset; exported data should include coverage and manifest metadata.]

## Skill Version(s):

2.4.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
