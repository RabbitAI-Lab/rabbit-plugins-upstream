## Description:

Routes users who are unsure which Buddhist master or teaching mode to consult to the appropriate master, curriculum, debate, or comparison skill without answering doctrinal or practice questions itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user needs help choosing which Buddhist master or teaching mode to consult. It returns a concise destination and reason, then leaves doctrinal and practice answers to the selected target skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may invoke on broad help-me-choose wording when the user expected general assistance.

Mitigation: Use it only for routing questions where the user is unsure which master or teaching mode to use, and stop after giving the destination.

Risk: Router output could be mistaken for doctrinal or practice guidance.

Mitigation: Keep responses to the destination and a short reason, and hand off doctrinal or practice questions to the selected master skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xr843/skills/master-help)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Markdown recommendation with a destination and short reason]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Router output only; it should not provide doctrinal explanations, practice advice, or scripture citations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
