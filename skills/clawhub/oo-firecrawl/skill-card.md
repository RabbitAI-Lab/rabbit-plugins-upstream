## Description:

Use this skill for Firecrawl requests that read, create, update, or delete Firecrawl data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Firecrawl scraping, search, crawl, extraction, URL mapping, LLMs.txt, deep research, agent-job, status, queue, credit, and token-usage actions through OOMOL's oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute shell or PowerShell from the network.

Mitigation: Verify the installer through a trusted, version-pinned source before running setup commands.

Risk: Some Firecrawl actions can change state or cancel/delete work.

Mitigation: Confirm the exact payload and expected effect before approving actions marked write or destructive.

## Reference(s):

- [Firecrawl homepage](https://www.firecrawl.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Firecrawl skill](https://clawhub.ai/oomol/skills/oo-firecrawl)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill relies on live Firecrawl action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
