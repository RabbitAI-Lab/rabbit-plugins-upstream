## Description:

XinJianXue Custom Advisor helps agents onboard to the XinJianXue API and, with user confirmation, request relationship, personality, behavior, and emotional guidance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to configure a user-defined XinJianXue advisor, complete account binding, and request reports for relationship, personality, behavior, and emotional guidance after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report calls send personal details to www.xinjianxue.com for processing.

Mitigation: Ask for explicit confirmation before each analysis and collect only the required subject details.

Risk: The generated license and api_key are sensitive account credentials.

Mitigation: Store credentials only in an OS keychain or dedicated credential store, and never expose them in chat, long-term memory, or configuration files.

Risk: Report calls consume account tokens through a paid API integration.

Mitigation: Disclose token use before report calls and surface insufficient-token responses without retrying blindly.

Risk: Returned reports may contain instruction-like phrasing.

Mitigation: Treat reports as reference data only and follow the local skill instructions for agent behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-assistant-global)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)
- [XinJianXue official site](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and HTTP endpoint instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation, dedicated credential storage, and account tokens before report calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
