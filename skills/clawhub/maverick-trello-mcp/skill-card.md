## Description:

Search and review Trello boards, lists, and cards, and create or update cards and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maverick](https://clawhub.ai/user/maverick)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use an agent to search and inspect Trello boards, lists, and cards, and to create or update cards and post comments for task coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unintended write can change shared Trello board content or post a comment.

Mitigation: Require clear user intent, read the current board or card state before changing it, and use read-only credentials when only viewing is needed.

## Reference(s):

- [Trello skill on ClawHub](https://clawhub.ai/maverick/skills/maverick-trello-mcp)
- [Trello API](https://api.trello.com/1)
- [mcporter](https://github.com/steipete/mcporter)
- [uv documentation](https://docs.astral.sh/uv/)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured Trello records and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results reflect Trello data and actions requested by the user.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
