## Description:

Serpdog helps agents run Serpdog search and account or quota read actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Serpdog action schemas, run Google Search, News, Videos, and Autocomplete queries, and retrieve Serpdog account and quota information through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official package manager, or download, inspect, and verify the installer before execution.

Risk: Serpdog searches and account or quota reads run through the user's connected OOMOL account.

Mitigation: Use the skill only when the OOMOL publisher and connected account are trusted for the intended query data.

## Reference(s):

- [Serpdog homepage](https://serpdog.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-serpdog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data and execution metadata from Serpdog connector actions.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
