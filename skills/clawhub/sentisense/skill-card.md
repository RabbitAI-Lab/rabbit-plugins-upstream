## Description:

SentiSense gives agents read-only access to U.S. stock market data including sentiment, prices, insider and congressional trades, institutional holdings, options positioning, analyst ratings, earnings, and AI-generated market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to query SentiSense financial market APIs for research, dashboards, screeners, and analysis workflows without trading or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial market information may be misread as investment advice.

Mitigation: Present outputs as informational research data only and avoid using them as personalized recommendations or trade instructions.

Risk: The skill sends financial-data queries and the SentiSense API key to SentiSense.

Mitigation: Use the SENTISENSE_API_KEY environment variable, rotate or revoke keys when needed, and use optional local CLI credential storage only when intentionally chosen.

Risk: API usage may consume quota or hit rate limits.

Mitigation: Account for Free and PRO tier limits, handle rate-limit responses, and batch or cache requests where appropriate.

## Reference(s):

- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Homepage](https://sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)
- [Current SentiSense Skill File](https://sentisense.ai/skill.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with API endpoint examples, shell commands, and JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance; responses depend on SentiSense API tier, quota, and rate limits.]

## Skill Version(s):

2.12.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
