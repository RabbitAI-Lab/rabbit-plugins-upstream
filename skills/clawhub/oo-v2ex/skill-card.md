## Description:

V2EX (v2ex.com). Use this skill for ANY V2EX request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate V2EX through an OOMOL-connected account, including reading topics, replies, nodes, notifications, member profiles, and token metadata. It can also run state-changing V2EX actions such as token creation, topic boosting, sticky changes, and notification deletion when confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands for the oo CLI.

Mitigation: Verify the oo CLI source and installation guide before running installer commands, and avoid executing remote scripts blindly.

Risk: The skill can perform state-changing V2EX actions, including token creation, topic boosting, sticky changes, and notification deletion.

Mitigation: Require explicit user confirmation of the exact action, target, payload, and expected effect before running any write or destructive action.

Risk: One state-changing action is not tagged for confirmation in the skill evidence.

Mitigation: Treat topic boosting as a write action and require confirmation even if the action list does not mark it with a write tag.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-v2ex)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [V2EX](https://www.v2ex.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live V2EX connector action schemas before constructing payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
