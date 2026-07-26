## Description: <br>
Creates pending HiJavis to-do cards from brainstorm-worthy voice or keyboard units, carrying a ready-to-paste prompt that hands captured transcript context to Claude's content-brainstorming flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samuel-wei](https://clawhub.ai/user/samuel-wei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External HiJavis users use this skill to turn voice notes or keyboard input into pending brainstorm cards that preserve the source session and provide a prompt for a Claude brainstorming session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can examine every completed HiJavis voice or keyboard unit when enabled, so sensitive conversations may be processed while it decides whether a card is warranted. <br>
Mitigation: Enable it only for users comfortable with broad transcript review, and review generated pending cards and chat digests before confirming or acting on them. <br>
Risk: The skill can create pending calendar cards and chat summaries without a pre-run confirmation. <br>
Mitigation: Use the Calendar tab Confirm/Discard gate to discard unwanted cards and avoid treating generated prompts as final output without review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/samuel-wei/skills/javis-brainstorming) <br>
- [HiJavis iPhone App](https://apps.apple.com/us/app/hijavis/id6745134765) <br>
- [to-do card contract](references/todo-card-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON payloads and Markdown digest text with Node.js shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates at most one pending to-do card per brainstorm-worthy unit; no card is emitted when no discernible goal is found.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
