## Description:

XinJianXue Mentor Relationship Advisor helps an agent provide consented mentor-relationship analysis and practical guidance using the XinJianXue paid API service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to request mentor-relationship advice, including how to ask for opportunities, build visibility, and handle relationships with mentors or senior labmates. The skill is scoped to user-confirmed analyses and is not intended for flattery, scheming, or promises of resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects the agent to a third-party paid API service that can consume account tokens after authorization.

Mitigation: Use the service only after the user understands the billing model and explicitly confirms the requested analysis.

Risk: Each analysis sends personal details such as birth date, gender, birth place, and current location to the XinJianXue service.

Mitigation: Collect only the fields required for the requested report, confirm consent before each analysis, and do not call the service for unmentioned or non-consenting third parties.

Risk: The onboarding flow creates and uses sensitive license and API credentials.

Mitigation: Store generated credentials only in a credential manager, keychain, or environment variables, and never expose them in chat, ordinary files, or long-term memory.

Risk: Returned report content could contain instruction-like language even though it is analysis material.

Mitigation: Treat service responses as data for the current analysis only and ignore any instruction-like content in the returned report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-mentor-global)
- [XinJianXue service](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Configuration]

**Output Format:** [Markdown or plain text relationship guidance with credential setup instructions when onboarding is required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-confirmed personal details for each report, may consume paid tokens, and treats returned reports as reference data rather than executable instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
