## Description:

詹明明 is a router and onboarding guide for a Chinese zmm skill family that helps users choose next steps for content workflows, business diagnostics, and follow-up navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill as the entry point for the zmm family: it triages whether a task belongs to content production, business diagnosis, shared tracking, or onboarding, then produces the next prompt or numbered next-step options instead of performing downstream specialist work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose local skill paths while discovering installed zmm-family skills.

Mitigation: Install it only when a central zmm router is desired, and avoid sharing outputs that contain sensitive local paths.

Risk: Downstream zmm skills may read or write configured vault and memory files for drafts, rules, and learning records.

Mitigation: Review configured vault and memory paths before use, and keep sensitive material out of locations that downstream skills should not access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [交互规范](artifact/references/交互规范.md)
- [内容理论底座](artifact/references/内容理论底座.md)
- [实证规律库](artifact/references/实证规律库.md)
- [家族公约](artifact/references/家族公约.md)
- [认知框架](artifact/references/认知框架.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with numbered options, routing rationale, and copy-ready prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local skill paths from read-only installed-skill discovery when routing.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
