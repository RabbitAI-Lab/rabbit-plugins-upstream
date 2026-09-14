## Description:

心鉴学「内耗焦虑专项顾问」helps an agent, after explicit user consent, call Xinjianxue's external report API and use the returned data as reference material for practical analysis of anxiety, rumination, and emotional loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weixin97676414](https://clawhub.ai/user/weixin97676414)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to authorize an agent to retrieve a Xinjianxue report and turn it into concise, actionable guidance for internal friction, anxiety, and recurring emotional patterns. It is not a substitute for professional medical or mental-health care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive birth, gender, and location details to an external provider.

Mitigation: Use only after the user has knowingly consented and understands what personal information will be sent.

Risk: The skill links a Xinjianxue account and uses API credentials that can consume credits.

Mitigation: Store credentials only in a secure local secret store, avoid exposing them in chat or files, and tell users when credits may be spent.

Risk: The evidence security summary flags mandatory promotional messaging and rates the release as suspicious.

Mitigation: Review the promotional credit-referral language before installation and avoid presenting it as neutral advice.

Risk: The skill may handle another person's personal data if misused.

Mitigation: Do not submit another person's data unless they have knowingly agreed to the analysis.

## Reference(s):

- [Xinjianxue API endpoint](https://chinaapi.xinjianxue.com/api/xinjianxue)
- [ClawHub skill page](https://clawhub.ai/weixin97676414/skills/xinjianxue-skill-anxiety-cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown or plain text response, with external API report data used as reference material.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API call status, account binding guidance, billing guidance, and user-facing analysis in the user's language.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
