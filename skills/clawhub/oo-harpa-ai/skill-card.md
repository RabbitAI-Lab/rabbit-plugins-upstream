## Description:

Operate HARPA AI through an OOMOL-connected account to run HARPA commands, execute prompts, scrape web pages, and search the web.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate HARPA AI from an agent through an OOMOL-connected browser session for prompts, commands, page scraping, and web search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may run downloaded installer code for the oo CLI.

Mitigation: Review and prefer verified OOMOL installation instructions before running installer scripts.

Risk: HARPA AI actions can include destructive commands in a connected browser session.

Mitigation: Require explicit user approval for any HARPA command that may change, overwrite, delete, or otherwise act through the connected browser.

## Reference(s):

- [HARPA AI homepage](https://harpa.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs through the oo CLI against a connected HARPA AI browser node; command responses include data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
