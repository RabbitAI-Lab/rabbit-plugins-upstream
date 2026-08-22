## Description:

Iran Chem Database helps agents deploy and operate a crawler-backed system that discovers, mirrors, parses, validates, and exports a measured best-effort index of chemical offerings from configured public Iranian supplier catalogues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and procurement researchers use this skill to install and operate a best-effort chemical supplier catalogue index, inspect crawl coverage, and export auditable molecule or offering datasets.

### Deployment Geography for Use:

Global, subject to authorization to crawl configured supplier sites and applicable regional rules.

## Known Risks and Mitigations:

Risk: The crawler may access and archive configured supplier websites without sufficient authorization.

Mitigation: Run it only for sites you are authorized to crawl and archive, respect site terms and robots.txt, and keep polite crawling limits enabled.

Risk: Free-access and archive fetchers can disclose target URLs to third-party services such as Jina, Wayback, Common Crawl, Translate, and related services.

Mitigation: Disable free_access, SPN2, Translate, Jina, Wayback, Common Crawl, and similar methods unless policy explicitly permits those disclosures; use egress allowlists where possible.

Risk: The API and dashboard are trusted-network services by default.

Mitigation: Place authentication in front of the API and dashboard before exposing them beyond a trusted network, and use TLS at the edge.

Risk: The .env file is sourced as shell during installation.

Mitigation: Review .env before running install steps, set a strong DB_PASSWORD, and avoid using environment files from untrusted sources.

Risk: Published README verification hashes may not match the inspected files.

Mitigation: Use the server-provided release hash, source fingerprint, and fileHashes evidence for integrity checks rather than relying only on README hash text.

Risk: Crawler output and mirrored pages can consume significant storage.

Mitigation: Set storage limits and scope crawl targets to the supplier domains needed for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database)
- [README](README.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api_reference.md)
- [Deployment Guide](docs/deployment_guide.md)
- [Adding Suppliers](docs/adding_suppliers.md)
- [HTTrack Integration Guide](docs/httrack_integration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and API/export instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide API exports that produce CSV, JSON, SDF, or manifest files after the deployed service has crawled configured suppliers.]

## Skill Version(s):

2.9.0 (source: server release metadata and SKILL.md frontmatter; pyproject.toml reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
