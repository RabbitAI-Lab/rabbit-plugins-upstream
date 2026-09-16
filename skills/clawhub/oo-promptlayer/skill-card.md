## Description:

PromptLayer helps an agent search and read prompt templates, logged requests, Tables, sheets, and sheet rows through an OOMOL-connected PromptLayer account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve PromptLayer prompt templates, request logs, and Table data from an authenticated workspace without handling raw PromptLayer tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not allow an agent to run those installers automatically; verify the oo CLI source first, install without elevated privileges, and use the platform install guide when setup is required.

Risk: Connecting PromptLayer through OOMOL can expose workspace prompt templates, logs, and Table data to the connected account workflow.

Mitigation: Connect only workspaces whose data may be accessed through OOMOL, and limit use to the listed read actions unless a future release documents write behavior.

## Reference(s):

- [PromptLayer homepage](https://promptlayer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-promptlayer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses are expected as JSON from the oo CLI when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
