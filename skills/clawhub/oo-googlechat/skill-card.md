## Description:

Google Chat helps an agent read Google Chat spaces and messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users can have an agent retrieve Google Chat spaces and message history from their OOMOL-connected account for requested chat review and lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can read Google Chat spaces and messages available to the connected account, including sensitive workplace chats requested by a prompt.

Mitigation: Install only for users who accept that read access, keep prompts specific to intended spaces or messages, and avoid broad retrieval over confidential chats.

Risk: First-time use depends on the OOMOL CLI install and OAuth connection flow.

Mitigation: Review the OOMOL CLI installation and Google Chat OAuth connection before first use, and rely on the connector flow rather than sharing raw tokens with the agent.

## Reference(s):

- [ClawHub Google Chat skill page](https://clawhub.ai/oomol/skills/oo-googlechat)
- [Google Chat product page](https://workspace.google.com/products/chat/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return data with meta.executionId when actions are executed.]

## Skill Version(s):

1.0.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
