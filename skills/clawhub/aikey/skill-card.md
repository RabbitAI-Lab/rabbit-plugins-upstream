## Description:

Routes creators and business owners to the appropriate AI KEY skills, offering guided onboarding, ready-to-send prompts, and next-step navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent content creators and business owners use AI KEY to choose a relevant skill for content planning, writing, review, or business decisions, then receive a prompt or suggested next step. New users can follow a guided introduction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured vault and memory files may contain sensitive business or creator information.

Mitigation: Review configured vault and memory paths and limit access to material intended for the skill.

Risk: The workflow may write persistent memory or output files.

Mitigation: Review configured output paths and inspect saved material before sharing or publishing.

Risk: A daily version check may contact a public GitHub content endpoint.

Mitigation: Review network access expectations before use in restricted environments.

## Reference(s):

- [AI KEY release on ClawHub](https://clawhub.ai/iamzifei/skills/aikey)
- [AI KEY interaction guidelines](artifact/references/交互规范.md)
- [AI KEY rule cards](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and ready-to-send skill prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to other skills rather than completing their tasks, except during guided onboarding.]

## Skill Version(s):

0.3.11 (source: server-resolved ClawHub release; bundled frontmatter states 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
