## Description:

Firecrawl lets agents operate Firecrawl through an OOMOL-connected account for scraping, search, site mapping, crawls, batch scrapes, structured extraction, and usage or status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to run Firecrawl operations through OOMOL, including web scraping, search, crawling, extraction, job monitoring, usage checks, and cancellation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can run code on the user's machine.

Mitigation: Review the setup path before installing and prefer a verified or package-manager install of the oo CLI.

Risk: The skill can start write workflows or cancel Firecrawl jobs through the connected account.

Mitigation: Confirm the exact payload, target job, and expected effect before running write or destructive actions.

Risk: Firecrawl access is mediated through an OOMOL-connected account.

Mitigation: Use the skill only if you trust OOMOL and are comfortable connecting your Firecrawl account through OOMOL.

## Reference(s):

- [ClawHub Firecrawl Skill](https://clawhub.ai/oomol/skills/oo-firecrawl)
- [Firecrawl Homepage](https://www.firecrawl.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas and JSON responses; write and destructive Firecrawl actions require confirmation before execution.]

## Skill Version(s):

1.0.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
