## Description:

詹明明 is a Chinese-language routing and onboarding entry skill for the zmm skill family that helps creators and small business operators choose an appropriate downstream content or business workflow and prepare a ready-to-send prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small business operators use this entry skill to get oriented, classify their task, select one main downstream zmm skill with limited supporting skills, and receive a concise prompt they can send in the next step. It also supports post-task navigation by reading the prior result and suggesting numbered next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read configured content vault, memory files, and local installed zmm skill folders while choosing downstream skills.

Mitigation: Install it only in environments where those local files are intended to be available, and review configured paths before use.

Risk: The entry skill can route work to downstream zmm skills whose behavior is not proven by this skill card.

Mitigation: Review each downstream zmm skill separately before running prompts or workflows produced by this entry skill.

Risk: Routing or onboarding guidance may influence content or business decisions using local rules and memories that can be incomplete or stale.

Mitigation: Treat generated prompts and next-step options as proposals, verify important decisions against current evidence, and update or remove stale local memory records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iamzifei/skills/zmm)
- [Publisher Profile](https://clawhub.ai/user/iamzifei)
- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [实证规律库](references/实证规律库.md)
- [家族公约](references/家族公约.md)
- [理论框架选型与装配](references/理论框架选型与装配.md)
- [规则卡](references/规则卡.md)
- [认知框架](references/认知框架.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with routing recommendations, ready-to-send prompts, concise recaps, and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference locally discovered zmm skills and configured content or memory paths when available.]

## Skill Version(s):

0.2.14 (source: server release evidence; artifact frontmatter reports 0.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
