## Description:

The Official Board skill lets an agent search and read company, executive, biography, org chart, colleague, news, and watchlist data through OOMOL's connected account workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run read-only The Official Board lookups through the OOMOL CLI after the user has installed the CLI, signed in, and connected The Official Board.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read data available through the connected OOMOL account, including The Official Board watchlist changes.

Mitigation: Before installation or use, confirm the user trusts the OOMOL oo CLI and intentionally connected the OOMOL account to The Official Board.

Risk: Unexpected payloads can broaden a lookup beyond the user's intended company or executive.

Mitigation: Inspect the live connector schema before building a payload and keep each command limited to the user's requested lookup.

## Reference(s):

- [The Official Board homepage](https://www.theofficialboard.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-the-official-board)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload/response handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are read-oriented connector instructions and command results; connector responses are expected as JSON under data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
