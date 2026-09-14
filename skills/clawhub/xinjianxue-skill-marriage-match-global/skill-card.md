## Description:

XinJianXue Marriage & Partner Selection Advisor helps an agent provide relationship-fit guidance by calling the XinJianXue API after explicit user consent and account onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they explicitly want relationship or marriage compatibility guidance based on XinJianXue trait reports. The agent gathers required consent and personal details, performs account-bound API calls, and returns human-facing guidance rather than a marry/do-not-marry decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires sensitive account-binding credentials and API credentials.

Mitigation: Use only a trusted official integration context, treat the one-time authorization code like a password, and store generated API credentials only in a credential store.

Risk: The workflow sends personal birth and location details to www.xinjianxue.com for processing.

Mitigation: Run the analysis only after explicit consent and subject agreement, and avoid using the skill when the user has not clearly requested this service.

Risk: API calls are made under the user's account and may consume paid tokens.

Mitigation: Make token use clear before analysis and use billing checks only when the user asks about token consumption.

## Reference(s):

- [XinJianXue official site](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)
- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-marriage-match-global)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)

## Skill Output:

**Output Type(s):** [Guidance, Text, API Calls, Configuration]

**Output Format:** [Markdown or plain text with JSON request examples and HTTP endpoint guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit consent, account-bound credentials, and token billing before producing an analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
