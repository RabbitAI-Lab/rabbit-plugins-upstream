## Description:

提供钱筮法起卦与讲卦体验，支持六爻判断、卦象学习和本地卦册记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan195](https://clawhub.ai/user/xuan195)

### License/Terms of Use:

MIT

## Use Case:

面向希望以易经钱筮作文化体验或自我反思的用户，用于掷币起卦、阅读卦辞与相关注疏，并记录近期卜问。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Readings and personal notes may be saved locally in plaintext.

Mitigation: Avoid including sensitive background details, or ask the agent to skip saving; storage permissions depend on the host.

Risk: Legacy migration leaves the older journal copy in place.

Mitigation: After migration, review the old copy and remove it if it is no longer needed.

Risk: Users may treat a divination reading as professional advice.

Mitigation: Frame readings as cultural reflection and direct medical, legal, or investment decisions to qualified professionals.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xuan195/skills/bushi-dashi)
- [Persona and safety guidance](references/persona.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Conversational text, CLI JSON, and a local JSON journal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Journal entries are stored locally as JSON.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
