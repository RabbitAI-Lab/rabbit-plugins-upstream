## Description:

Operate xAI through an OOMOL-connected account by inspecting live connector schemas and running supported xAI actions with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to list xAI models, fetch model metadata, and create non-streaming chat completions through OOMOL-managed xAI connectivity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands from OOMOL endpoints.

Mitigation: Review the installer source and prefer a verified package-manager or documented installation path before executing installation commands.

Risk: Chat-completion requests may consume xAI or OOMOL account resources.

Mitigation: Inspect the live connector schema and confirm the exact chat-completion payload before running write actions.

Risk: Account authentication and xAI connection steps affect the user's OOMOL-connected account.

Mitigation: Run sign-in or connection flows only after an auth or connection failure and confirm the account context before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-x-ai)
- [xAI homepage](https://x.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution.]

## Skill Version(s):

1.0.4 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
