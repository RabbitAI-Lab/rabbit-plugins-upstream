## Description:

US stock market data API for AI agents: news and social sentiment, the SentiSense Score, the SentiSense Rating daily A to F letter grade, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query SentiSense's read-only financial intelligence API for stock sentiment, ratings, market data, insider and congressional trades, institutional flows, analyst signals, options intelligence, earnings data, and AI-generated market summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat financial information returned through the skill as investment advice or trading instructions.

Mitigation: Present SentiSense responses as informational market data only and require human judgment before any investment decision.

Risk: Authenticated API calls use SENTISENSE_API_KEY and may consume free or paid quota.

Mitigation: Load the key from the environment, avoid logging it, monitor usage, and rotate or revoke the key from SentiSense when needed.

## Reference(s):

- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Website](https://sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Latest SentiSense Skill File](https://sentisense.ai/skill.md)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API endpoint descriptions, JSON response shapes, and curl, Python, and JavaScript examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance requiring SENTISENSE_API_KEY; responses may be quota-gated, tier-limited, previewed, or delayed depending on endpoint and account tier.]

## Skill Version(s):

2.12.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
