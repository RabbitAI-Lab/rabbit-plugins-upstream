## Description:

Analyzes construction tender opportunities using Zhiliaobiaoxun bid-history data to help assess whether to bid, likely competitors, pricing references, qualification risks, and decision rationale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commercial teams use this skill to evaluate construction-project tenders, compare buyer history and likely competitors, estimate pricing ranges, and produce a bid/no-bid decision report. It is intended for public tender-data analysis and should be reviewed as supporting evidence, not as the sole basis for a commercial decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender queries and account data are sent to the third-party vendor API.

Mitigation: Install and use the skill only when the vendor is trusted for the project names, company names, and account data involved.

Risk: Automatic registration can send a hardware-derived device fingerprint to the vendor.

Mitigation: Prefer configuring ZLBX_API_KEY directly, or decline automatic registration when device-derived registration is not acceptable.

Risk: API keys are stored locally in ~/.zlbx/config.json when automatic registration succeeds.

Mitigation: Protect the local configuration file and avoid exposing API keys in prompts, logs, reports, or shared terminals.

Risk: Generated report links may include signed access parameters.

Mitigation: Treat generated HTML reports and cited source links as share-sensitive and remove or regenerate them when broad sharing is not intended.

Risk: Bid recommendations and competitor assessments can affect commercial decisions and reputational judgments.

Mitigation: Review the report's cited data, data gaps, and disclaimer before relying on the recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/construction-tender-bid-decision)
- [Publisher profile](https://clawhub.ai/user/dragonzu)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account API base](https://ai.zhiliaobiaoxun.com/web-api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full reports are described as about 12-25 API calls or credits; quick reports are described as about 5-8 calls or credits.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
