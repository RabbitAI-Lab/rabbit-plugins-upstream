## Description:

Queries zodiac profiles and daily, weekly, monthly, or yearly horoscope readings through Juhe Data, with paid access handled through an A2M/HTTP 402 flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to request a zodiac sign profile or horoscope reading for a selected sign and time period. The skill is intended for paid entertainment queries and routes payment through Alipay before presenting returned results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat entertainment horoscope output as decision guidance.

Mitigation: Present the entertainment-only disclaimer and avoid using the output for medical, financial, legal, career, or relationship decisions.

Risk: The skill initiates a paid flow through Alipay payment capabilities.

Mitigation: Confirm the price, order details, and user intent before payment, and stop the flow if the user cancels.

Risk: The query sends the selected zodiac sign and period to a third-party API.

Mitigation: Send only the requested sign and period over the fixed HTTPS endpoint and do not add personal identifiers or unrelated user data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/juhemcp/skills/juhe-constellation-a2a)
- [ClawHub Publisher Profile](https://clawhub.ai/user/juhemcp)
- [Juhe A2A Query Endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns structured horoscope and zodiac-profile content from the service response, with an entertainment-only disclaimer.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
