## Description:

Skyvern helps agents operate Skyvern browser automation through an OOMOL-connected account for reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Skyvern connector schemas, start browser automation tasks, list and inspect runs, and cancel active runs through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Launching Skyvern browser automation can change websites, accounts, billing, or external data.

Mitigation: Require explicit user confirmation before starting run_task automation or canceling active runs, and confirm the exact JSON payload and intended effect.

Risk: First-time setup includes installing the oo CLI from a remote script.

Mitigation: Review setup commands before installation and prefer official, versioned, verifiable oo CLI installation instructions.

## Reference(s):

- [Skyvern homepage](https://www.skyvern.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skyvern)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector execution IDs, run details, screenshots, hosted file links, and recording URLs returned by Skyvern actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
