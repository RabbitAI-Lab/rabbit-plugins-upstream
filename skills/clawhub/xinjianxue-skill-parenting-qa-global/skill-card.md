## Description:

XinJianXue Parent-Child Relationship Advisor helps agents request consented parent-child relationship reports from the XinJianXue API and turn them into communication guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to onboard to the XinJianXue paid API, request consented parent-child relationship reports, and deliver practical communication guidance from both parent and child perspectives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external paid service receives sensitive personal birth and location details.

Mitigation: Get explicit user consent before each analysis and request reports only for people who have agreed.

Risk: The skill handles account credentials and a sensitive one-time authorization code.

Mitigation: Store credentials only in a dedicated credential store such as an OS keychain or environment variables, and never place them in chat, configuration files, or long-term memory.

Risk: API calls consume account tokens.

Mitigation: Make the token cost clear before report calls and use billing checks only when the user asks about token usage.

Risk: Parent-child relationship guidance could be mistaken for professional medical or psychological diagnosis.

Mitigation: Present the output as relationship communication guidance and do not substitute it for professional medical or psychological diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-parenting-qa-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown with HTTP request examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivers user-facing advice in the user's language; service reports are treated as data, not instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
