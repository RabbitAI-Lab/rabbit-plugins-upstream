## Description:

Capture and co-develop a user's new product, feature, experience, architecture, or creative-workflow idea into one traceable, AI-friendly Markdown document without starting implementation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[isdou](https://clawhub.ai/user/isdou)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to capture early product, feature, architecture, experience, or creative-workflow ideas as a living Markdown record before implementation starts. It helps preserve the original intent, decisions, open questions, and implementation authorization state for later handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may trigger implicitly and create or update Markdown idea records when a message is interpreted as a new idea.

Mitigation: Use explicit wording when requesting immediate implementation, and review the reported document path, status, and implementation authorization after each capture.

Risk: Persistent idea records may surprise users who do not want repository documentation changed by idea exploration.

Mitigation: Install or invoke the skill only in repositories where persistent Markdown idea records are desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/isdou/skills/i-have-an-idea)
- [Idea record template](assets/idea-record-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [A single Markdown idea record plus brief conversational status updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates one living idea document, usually under docs/ideas/, after checking for related Markdown records.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
