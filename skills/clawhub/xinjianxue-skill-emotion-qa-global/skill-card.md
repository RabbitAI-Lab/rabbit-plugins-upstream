## Description:

XinJianXue Romantic Relationship Advisor helps an agent collect consented relationship-analysis inputs, call the XinJianXue API, and turn the returned report into direct emotional guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent act as a XinJianXue Romantic Relationship Advisor for relationship questions after explicit consent. The agent handles onboarding, credential use, paid API report calls, and user-facing guidance based on returned report data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal details such as birth, gender, and location data to www.xinjianxue.com for report generation.

Mitigation: Use the skill only after explicit consent for the specific analysis and confirm the required personal details before each paid report call.

Risk: The skill requires account binding and stores service credentials for later API calls.

Mitigation: Store credentials only in a protected credential manager or equivalent dedicated secret storage, and never expose them in conversation or configuration files.

Risk: Report calls consume XinJianXue service tokens.

Mitigation: Confirm the user wants a paid report before sending data, and disclose token usage before making report calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-emotion-qa-global)
- [Publisher Profile](https://clawhub.ai/user/weixin97676414)
- [XinJianXue Service](https://www.xinjianxue.com)
- [XinJianXue API Base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, API Calls, Configuration]

**Output Format:** [Markdown or plain text guidance with HTTP request details when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires consented personal details, account-bound credentials, and token consumption for report calls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
