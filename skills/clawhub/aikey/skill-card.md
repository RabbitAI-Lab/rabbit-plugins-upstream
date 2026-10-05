## Description:

Routes creators and business operators to AI KEY skills for content work or business decisions, with guided onboarding and next-step navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent content creators and business operators use this entry point to find an appropriate skill for their task, try a guided first run, or choose a next step after completing a task. It prepares a prompt for a downstream skill rather than performing the full analysis or writing itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broader AI KEY workflow may read local project, vault, and configuration files outside the intended task scope.

Mitigation: Review configured paths before use and limit them to the workspace you intend to share.

Risk: The broader workflow may persist drafts or memory records in local files.

Mitigation: Review the configured draft and memory locations and inspect proposed changes before retaining them.

## Reference(s):

- [AI KEY on ClawHub](https://clawhub.ai/iamzifei/skills/aikey)
- [Interaction guidelines](references/交互规范.md)
- [Family conventions](references/家族公约.md)
- [Decision rules](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Conversational text with a suggested skill route and ready-to-send prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a guided onboarding example or numbered next-step choices.]

## Skill Version(s):

0.3.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
