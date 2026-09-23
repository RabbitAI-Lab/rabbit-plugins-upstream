## Description:

AI KEY routes an agent between content-creation and business-operations workflows, offering guided onboarding, pre-task skill selection, prompt handoff, and post-task navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, business operators, and agents use this skill as an entry point for choosing the right AI KEY workflow, preparing the next prompt, or deciding the next step after another AI KEY skill returns results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local AI KEY configuration, memory, and vault-related paths while routing work.

Mitigation: Review configured vault and memory locations before use, and avoid using it with private business or content data unless that local access is acceptable.

Risk: The bundled discovery script lists installed AI KEY-family skills and their real filesystem paths.

Mitigation: Inspect script output before sharing a session transcript or generated routing response outside the local environment.

Risk: Broad natural-language triggers may route into the skill when the user intended a narrower workflow.

Mitigation: Prefer explicit /aikey commands and confirm the selected downstream skill before acting on sensitive material.

## Reference(s):

- [AI KEY ClawHub listing](https://clawhub.ai/iamzifei/skills/aikey)
- [AI KEY README upgrade note](https://github.com/iamzifei/aikey#老用户升级zmm-已改名为-ai-key)
- [Interaction Guidelines](references/交互规范.md)
- [Content Theory Foundation](references/内容理论底座.md)
- [Empirical Rules Library](references/实证规律库.md)
- [AI KEY Family Convention](references/家族公约.md)
- [Theory Framework Selection and Assembly](references/理论框架选型与装配.md)
- [Rule Cards](references/规则卡.md)
- [Cognitive Framework](references/认知框架.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, numbered options, and ready-to-send prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local AI KEY configuration, vault paths, memory files, and installed-skill metadata when routing.]

## Skill Version(s):

0.3.8 (source: server release metadata; artifact frontmatter reports 0.3.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
