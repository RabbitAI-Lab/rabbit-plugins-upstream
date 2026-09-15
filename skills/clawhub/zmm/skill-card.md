## Description:

Routes users to the appropriate zmm content or business skill, supports guided onboarding, and returns ready-to-send prompts for downstream skills without performing the downstream diagnosis itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small business operators use this entry-point skill to choose the right zmm workflow for content planning, scripting, review, retrospectives, revenue analysis, concentration risk, dependency risk, and decisions. It is intended to route work, generate a prompt for the next skill, or provide a guided onboarding path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read zmm config, vault paths, installed zmm skill descriptions, and skill memory.

Mitigation: Install only when those sources are intended to be available to the agent, and keep the configured memory directory narrow and reviewable.

Risk: Conversational feedback can become persistent rules used by later skill runs.

Mitigation: Review saved feedback before treating it as an active rule, and prefer a confirmation step before feedback is persisted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [实证规律库](references/实证规律库.md)
- [zmm 技能家族公约](references/家族公约.md)
- [理论框架选型与装配](references/理论框架选型与装配.md)
- [规则卡](references/规则卡.md)
- [认知框架](references/认知框架.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with numbered options, brief rationale, and quoted prompts for downstream skills.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a shell command for installed-skill discovery when the runtime environment permits it.]

## Skill Version(s):

0.2.9 (source: ClawHub release metadata; artifact frontmatter reports 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
