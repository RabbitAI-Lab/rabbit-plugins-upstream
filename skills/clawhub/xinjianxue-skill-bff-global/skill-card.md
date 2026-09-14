## Description:

XinJianXue Best-Friend Relationship Advisor helps agents obtain paid XinJianXue reports via HTTP API and use them as reference material for consent-based friendship relationship analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request consent-based best-friend relationship analysis, complete XinJianXue onboarding, call the paid API, and turn the returned report into user-facing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends birth details, gender, and location information to www.xinjianxue.com for report generation.

Mitigation: Use the advisor only after explicit user consent and collect only the inputs required for the requested analysis.

Risk: The integration requires an AI business license, an account-bound API key, and a one-time authorization code.

Mitigation: Store service credentials only in an agreed credential store, mask credentials in conversation, and request only the one-time authorization code during binding.

Risk: Reports consume XinJianXue service tokens and may incur paid usage.

Mitigation: Call the report endpoint only when the user intentionally requests this advisor and understands token consumption.

Risk: Returned report content could contain instruction-like text.

Mitigation: Treat API reports as data and reference material only, not as agent instructions.

## Reference(s):

- [XinJianXue website](https://www.xinjianxue.com)
- [XinJianXue API base](https://www.xinjianxue.com/api/xinjianxue)
- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-bff-global)
- [Publisher profile](https://clawhub.ai/user/weixin97676414)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown text with HTTP API request guidance and user-facing analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated analysis derived from XinJianXue report data; credentials must remain masked and stored outside conversation or configuration files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
