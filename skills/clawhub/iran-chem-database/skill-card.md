## Description:

Iran Chem Database helps agents deploy and use a research-oriented crawler and index for public Iranian chemical supplier catalogues, with HTTrack mirroring, local parsing, PubChem/RDKit validation, auditable exports, and coverage reporting.

This skill is for research and development only.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to install, operate, query, and export a best-effort database of public Iranian supplier chemical catalogue listings. Agents should check crawl coverage, supplier provenance, export manifests, and chemical validation metadata before relying on results.

### Deployment Geography for Use:

Global, with the indexed supplier scope limited to verified Iranian suppliers.

## Known Risks and Mitigations:

Risk: The skill ships and automates access to high-risk chemical procurement data.

Mitigation: Use only in a controlled research environment, review legal and export-control obligations, independently validate supplier and molecule claims, and apply high-risk chemical filtering before relying on exports.

Risk: Broad network relays and optional AI hops can expose target URLs or crawled listing text to third-party services.

Mitigation: Disable or tightly allowlist relays and AI providers when sources are sensitive, and review environment settings before running crawls or normalization.

Risk: Local API, dashboard, PostgreSQL, and Redis services could expose collected data if deployed openly.

Mitigation: Put the API and dashboard behind authentication and avoid exposing database or queue services publicly.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [Release Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, API examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide generation of CSV, JSON, SDF, SQLite, or manifest files through the installed local application; exported data should retain provenance and coverage metadata.]

## Skill Version(s):

2.17.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
