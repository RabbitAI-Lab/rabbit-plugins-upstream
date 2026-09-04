## Description:

This skill lets an agent search and read Tongcheng Chengxin (ly.com) travel data through the OOMOL chengxin connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Tongcheng Chengxin for attractions, buses, flights, hotels, trains, multimodal transport, and travel products through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search queries may be sent through OOMOL and Tongcheng Chengxin as part of connector use.

Mitigation: Install and use the skill only when that data flow is intended for the user's OOMOL-connected account.

Risk: The oo CLI, account sign-in, connector connection, or billing state may block action execution.

Mitigation: Use the documented one-time setup and fallback steps only after a command fails with the matching auth, connection, or billing error.

Risk: Incorrect action payloads can produce failed or misleading search results.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [Tongcheng Chengxin homepage](https://www.ly.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chengxin)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
