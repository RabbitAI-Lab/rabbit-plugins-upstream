## Description:

Scrapingdog helps agents fetch web pages and retrieve parsed Google Search, Google Scholar, Google Maps, place, usage, and credit data through OOMOL-connected Scrapingdog actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Scrapingdog read actions for web HTML fetching, parsed Google Search, Google Scholar, Google Maps lookups, and account usage checks through OOMOL-connected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests piping remote installer scripts directly into a shell.

Mitigation: Prefer an official package manager or a downloaded, version-pinned installer with signature or checksum verification before installation.

Risk: Scrapingdog actions can process target URLs and account usage data.

Mitigation: Review target URLs and account data before running connector actions, and keep credentials scoped to the Scrapingdog connection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-scrapingdog)
- [Scrapingdog Homepage](https://www.scrapingdog.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects with data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
