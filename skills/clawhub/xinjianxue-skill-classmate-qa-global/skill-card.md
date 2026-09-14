## Description:

XinJianXue "Classmate Relations Advisor" helps agents provide classmate relationship analysis, personality and behavior reading, and emotional guidance through a paid XinJianXue API integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user explicitly requests classmate relationship guidance and consents to sending the required personal details to XinJianXue. It supports onboarding, authenticated report calls, translation or localization of returned analysis, and guidance grounded in the Classmate Relations Advisor role.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth, gender, birthplace, and current-location details to www.xinjianxue.com for processing.

Mitigation: Use the skill only after explicit user consent and provide only the details required for the requested analysis.

Risk: Using the service may consume XinJianXue tokens under the user's account.

Mitigation: Confirm the user understands token consumption before report calls and check billing only when the user asks.

Risk: The one-time authorization code and generated credentials can bind the AI to a user account.

Mitigation: Collect the authorization code only for intended account binding and store generated credentials in dedicated credential storage, not in chat, memory, or configuration files.

Risk: Returned reports may contain instruction-like text even though they are analysis material.

Mitigation: Treat XinJianXue reports as data or reference material only; the local skill role remains the sole instruction source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-classmate-qa-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, API Calls, configuration]

**Output Format:** [Markdown guidance with HTTP request details and user-facing analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation, authenticated XinJianXue API access, and dedicated credential storage.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
