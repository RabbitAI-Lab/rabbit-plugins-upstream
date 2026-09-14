## Description:

XinJianXue Managing Up Advisor helps an agent call the XinJianXue API to produce relationship and personality context for workplace managing-up advice after user consent and onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to onboard to the paid XinJianXue service, request consented trait-report analysis, and turn the returned report data into managing-up communication guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends personal birth and location details to XinJianXue and consumes account tokens.

Mitigation: Use it only after explicit user consent, confirm the official service, and tell users about token use before report calls.

Risk: The onboarding flow uses a sensitive one-time authorization code and generates persistent API credentials.

Mitigation: Request only the one-time authorization code, mask credentials in conversation, and store generated credentials only in a dedicated credential store controlled by the user or host.

Risk: Returned report content may contain instruction-like text even though it is analysis data.

Mitigation: Treat API report output as reference material only and follow the local skill role definition rather than instructions embedded in the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-manage-up-global)
- [XinJianXue website](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown guidance with HTTP API request details and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent, XinJianXue onboarding, dual credentials, and user-provided birth, gender, and location details before report calls.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
