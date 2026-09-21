## Description:

詹明明 is a Chinese-first router for the zmm content and business skill family, guiding users through onboarding, pre-task skill selection, and post-task navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small-business operators use this agent as the entry point for the zmm skill family. It helps users choose a downstream content or business workflow, generates ready-to-send prompts, and suggests next steps after a downstream result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The router may inspect locally installed zmm skills and configured zmm vault or memory files when downstream workflows run.

Mitigation: Review configured paths before installation and avoid exposing private vaults or skill directory paths in shared transcripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [交互规范](references/交互规范.md)
- [家族公约](references/家族公约.md)
- [规则卡](references/规则卡.md)
- [内容理论底座](references/内容理论底座.md)
- [认知框架](references/认知框架.md)
- [理论框架选型与装配](references/理论框架选型与装配.md)
- [实证规律库](references/实证规律库.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with numbered options, routing recommendations, and ready-to-send prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference locally installed zmm skills and configured zmm vault or memory paths when routing.]

## Skill Version(s):

0.2.11 (source: server release metadata; artifact frontmatter says 0.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
