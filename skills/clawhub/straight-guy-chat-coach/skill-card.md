## Description:

Chinese-language chat coaching skill that decodes user-provided relationship messages with confidence labels, states what cannot be inferred, and suggests respectful reply options without manipulation, deception, or sending messages for the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to interpret Chinese relationship or messaging conversations, identify likely intent and uncertainty, and draft respectful response options. It is intended for advice and wording suggestions only; the user remains responsible for whether and how to send any message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may paste unnecessary personal details from private conversations.

Mitigation: Avoid sharing unnecessary personal data; the skill instructs agents to replace real names, phone numbers, addresses, employers, schools, and handles with placeholders in output.

Risk: Relationship advice can become manipulative, coercive, or encourage unwanted persistence.

Mitigation: The skill sets hard boundaries against PUA, deception, impersonation, repeated pursuit after rejection, and platform or account actions, and redirects users toward respectful communication or stopping contact.

Risk: The skill may be over-relied on for emotionally sensitive conversations.

Mitigation: The skill frames outputs as suggestions, requires uncertainty labels, names what cannot be inferred, and reminds users that they remain responsible for whether and how to send messages.

## Reference(s):

- [解码信号与关系阶段](references/decoding-and-stages.md)
- [红线与自检](references/redlines.md)
- [高频场景库](references/scenarios.md)
- [ClawHub skill page](https://clawhub.ai/419597334-sudo/skills/straight-guy-chat-coach)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured Markdown-like Chinese text with intent analysis, confidence, suggested replies, consequences, contraindications, rationale, and examples to avoid]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not call messaging platforms, request account authority, or send messages; outputs suggested wording for user review.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
