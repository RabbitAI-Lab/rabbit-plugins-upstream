## Description:

Typebot (typebot.com). Use this skill for ANY Typebot request: searching and reading data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent inspect Typebot workspaces, bots, definitions, and collected results through the OOMOL Typebot connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Typebot workspaces, bot definitions, and collected results through the connected OOMOL account.

Mitigation: Connect only the Typebot account and scopes the agent should access, and install the skill only where that read access is acceptable.

Risk: The skill may require installing or using the OOMOL oo CLI before connector actions can run.

Mitigation: Review the OOMOL CLI install step and use the first-time setup flow only after an auth, connection, or missing-command failure.

## Reference(s):

- [Typebot homepage](https://typebot.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Typebot skill page](https://clawhub.ai/oomol/skills/oo-typebot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
