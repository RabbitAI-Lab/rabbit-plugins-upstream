## Description:

Search the user's past AI coding sessions with the deja CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to search prior local AI coding sessions before re-debugging issues, re-deriving decisions, or changing files with relevant prior context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search local AI coding history, which may include sensitive project context from prior sessions.

Mitigation: Install and use it only where the agent is permitted to access local coding-session history, and avoid exposing recalled details unless they are relevant to the current task.

Risk: The deja remember workflow can store explicit decisions for later recall.

Mitigation: Store only settled, self-contained decisions that are appropriate for future local agent use.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-producing CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local coding-session history when the deja CLI or MCP tools are available.]

## Skill Version(s):

0.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
