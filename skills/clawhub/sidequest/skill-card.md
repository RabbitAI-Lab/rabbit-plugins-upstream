## Description:

Hire verified real people for paid real-world quests via SideQuest. Use when a task needs a human, such as calling a business, checking a store is open, taking photos at a place, inspecting an item, a pickup or return, waiting in line, native-speaker translation, or human review of AI output. Funds are held in escrow and released when you approve the proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uckhill](https://clawhub.ai/user/uckhill)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers can delegate paid real-world errands, information gathering, translation, and human review to verified people, then review submitted proof and approve or dispute the work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags an undisclosed $50 account top-up in the setup flow.

Mitigation: Confirm the planned balance with the account owner before setup, and use a capped agent key with per-quest and daily spending limits.

Risk: Payment approval and the sharing of task details with SideQuest and a tasker are not clearly explained; submitted quests are automatically approved after 72 hours.

Mitigation: Review the task brief and personal information before posting, enable per-quest approval when appropriate, and promptly review proof to approve or dispute it before the deadline.

## Reference(s):

- [SideQuest API guide](https://sidequestpays.com/llms.txt)
- [SideQuest OpenAPI specification](https://sidequestpays.com/openapi.json)
- [SideQuest service](https://sidequestpays.com)
- [ClawHub skill release](https://clawhub.ai/uckhill/skills/sidequest)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Text]

**Output Format:** [Markdown guidance with shell command examples and JSON API payloads; quest results include text and submitted proof details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quest posting spends prepaid funds; human review is needed to approve or dispute submitted work.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
