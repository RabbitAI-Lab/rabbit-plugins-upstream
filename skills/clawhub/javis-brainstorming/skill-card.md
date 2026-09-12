## Description:

Brainstorming turns recent HiJavis voice or keyboard transcripts with a discernible idea into a pending calendar to-do card containing a ready-to-paste prompt for Claude's content-brainstorming flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External HiJavis users use this skill to capture brainstorm-worthy voice notes or typed thoughts as pending calendar cards, then open the card's chat prompt to continue the planning session in Claude.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read recent private voice or keyboard transcripts and can create pending brainstorm cards before the user confirms them.

Mitigation: Enable it only with the intended internal Javis service, limit the gateway token to transcript-read and card/chat-write permissions, and review pending cards before confirming them.

## Reference(s):

- [Brainstorming ClawHub skill page](https://clawhub.ai/samuel-wei/skills/javis-brainstorming)
- [to-do card contract](references/todo-card-contract.md)
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Text]

**Output Format:** [JSON command output, pending to-do card payloads, and Markdown chat digests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit no card when the transcript does not contain a clear brainstorm-worthy goal or request.]

## Skill Version(s):

0.6.3 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
