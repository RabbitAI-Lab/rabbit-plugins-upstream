## Description:

Iran Chemical Database helps agents operate a live, auditable crawler and local database for best-effort indexing of configured public Iranian chemical supplier catalogues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and procurement analysts use this skill to install and operate a crawler-backed PostgreSQL, FastAPI, and Streamlit system for researching configured public Iranian chemical supplier catalogues. Agents should check coverage and verification status before relying on any supplier or molecule result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill ships sensitive chemical procurement data and can crawl public supplier catalogues.

Mitigation: Install only where the operator is authorized to crawl the configured sources and handle the resulting data; review or remove high-risk seed rows before use.

Risk: Broad relay, proxy, and cloud-egress paths may create unexpected network exposure.

Mitigation: Disable or tightly restrict relay and cloud-egress features unless explicitly needed, and monitor scheduled crawls and outbound traffic.

Risk: External AI-provider normalization paths may send crawled listing text outside the local environment.

Mitigation: Disable external AI-provider paths for sensitive sources or restrict them to approved providers and inputs.

Risk: Local API, dashboard, database, and worker services can expose crawler data if deployed without controls.

Mitigation: Bind local services behind authentication and deployment controls before making them reachable beyond the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [AI Agent Navigation & Chemical Extraction Masterclass](docs/AI_AGENT_NAVIGATION_AND_CRAWLING_GUIDE.md)
- [Per-Site Navigation & Fetch Playbook](docs/SITE_PLAYBOOK.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [Relay Integrity](docs/RELAY_INTEGRITY_ROUND10.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API endpoints, and configuration references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to local APIs, exports, seed data, and verification commands; initial crawl may be partial or running.]

## Skill Version(s):

2.36.1 (source: SKILL.md frontmatter, release evidence, CHANGELOG, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
