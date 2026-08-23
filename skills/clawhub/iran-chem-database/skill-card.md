## Description:

Iran Chem Database helps agents deploy and use a Linux service that crawls configured public Iranian chemical supplier catalogs, mirrors sources, extracts molecule listings, reports coverage, and exports auditable datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research analysts use this skill to set up and query a best-effort crawler-backed database of chemical supplier offerings, with coverage checks and export metadata before results are presented as complete.

### Deployment Geography for Use:

Global, with indexed supplier scope limited to verified Iranian suppliers.

## Known Risks and Mitigations:

Risk: The skill crawls and mirrors third-party supplier sites and public Telegram channels, which may raise authorization, terms-of-service, or acceptable-use concerns.

Mitigation: Install only in a controlled environment, confirm authorization before crawling, and disable scheduled crawling, discovery, free_access, social mirroring, or enrichment features that are not needed.

Risk: Broad/default network crawling and third-party fetchers can expand outbound data flows beyond the intended supplier set.

Mitigation: Use egress allowlists, storage limits, and trusted-network controls for the API, dashboard, Redis, and PostgreSQL services.

Risk: The shipped seed export includes high-impact chemical procurement data and channels marked unverified.

Mitigation: Treat the seed export as untrusted until re-verified and require coverage, supplier-verification, and export metadata checks before presenting results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [Seed Coverage Report](data/seed_export/coverage_report.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API query guidance, export instructions, coverage caveats, and deployment commands.]

## Skill Version(s):

2.14.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
