## Description: <br>
Read-only financial market data API. Stock prices, sentiment, insider trading, institutional flows, politician trades, AI insights. No trading, no purchases, no write operations, no wallet access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to let an agent retrieve SentiSense financial market data, sentiment, insider and politician trading disclosures, institutional flows, AI insights, market summaries, calendars, and related research signals through a read-only API. The skill is for informational research workflows and does not provide investment advice or enable trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent needs access to SENTISENSE_API_KEY to make API requests. <br>
Mitigation: Provide only the SentiSense API key required for this service, avoid exposing unrelated credentials, and rotate the key if it is shared outside the intended agent environment. <br>
Risk: Market data, AI insights, and sentiment outputs may be mistaken for investment advice. <br>
Mitigation: Use outputs as informational research only and require human review before making financial decisions. <br>
Risk: Quota-gated, rate-limited, or paid-tier endpoints can consume API allowance or require a PRO subscription. <br>
Mitigation: Check endpoint tier labels and monitor request volume before running broad data collection workflows. <br>


## Reference(s): <br>
- [SentiSense API documentation](https://sentisense.ai/docs/api/) <br>
- [SentiSense website](https://sentisense.ai) <br>
- [SentiSense live skill file](https://sentisense.ai/skill.md) <br>
- [SentiSense methodology](https://sentisense.ai/methodology#institution-rankings) <br>
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense) <br>
- [Publisher profile](https://clawhub.ai/user/thesentitrader) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with REST endpoint descriptions, curl commands, code snippets, and JSON response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SENTISENSE_API_KEY for authenticated read-only requests; some endpoints are rate-limited, quota-gated, preview-limited, or PRO-only.] <br>

## Skill Version(s): <br>
2.7.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
