## Description:

Operate Trent through an OOMOL-connected account using the oo CLI, including sending chat messages through Trent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with Trent from an agent session through the OOMOL oo CLI. The skill guides the agent to inspect the live connector schema, construct valid JSON payloads, and run supported Trent actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Prefer an official, versioned oo CLI installer with checksum or signature verification before installing.

Risk: The send_chat action changes Trent state by sending a message.

Mitigation: Confirm the exact payload and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trent)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Trent homepage](https://trent.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
