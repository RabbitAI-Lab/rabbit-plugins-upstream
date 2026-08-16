## Description:

A pre-bid due diligence assistant that analyzes a specific tender project, buyer history, likely competitors, comparable pricing, disqualification risks, and bid/no-bid recommendations using Zhiliaobiaoxun bidding data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

External business development, sales, and bidding teams use this skill before responding to a tender to decide whether to bid, estimate a defensible price range, and identify buyer, competitor, qualification, and data-gap risks. It produces a decision-oriented report from user-provided tender details and Zhiliaobiaoxun public bidding data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or use a local provider account and perform device-based auto-registration when no API key is already configured.

Mitigation: Set ZLBX_API_KEY yourself before use, or decline automatic registration and use the provider's manual account flow.

Risk: The skill stores credentials under the user's home directory and saves generated bid reports locally by default.

Mitigation: Review local credential and report locations, restrict file permissions where appropriate, and remove reports that are no longer needed.

Risk: Generated reports can contain signed access links to bidding records and may be shared outside the original analysis context.

Mitigation: Review generated reports before sharing, remove links that should not be redistributed, and treat report files as sensitive business documents.

Risk: Bid recommendations can affect commercial decisions and may rely on incomplete, stale, or unavailable public bidding data.

Mitigation: Use the report as decision support only, review cited evidence and data gaps, and require human approval before acting on the recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dragonzu/skills/pre-bid-analysis-assistant)
- [API quick reference](artifact/references/api-quick.md)
- [Analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API v2 endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{tool})
- [Zhiliaobiaoxun business portal](https://agent.zhiliaobiaoxun.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown decision report with optional self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited bidding records and locally saved HTML reports; expected full analysis consumes about 12-25 paid query credits, while quick analysis consumes about 5-8 credits.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
