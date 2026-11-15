## Description:

Builds a 13-week rolling cash flow forecast from QuickBooks Online data with base, optimistic, and pessimistic scenarios for cash runway, burn rate, and liquidity planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samledger67-dotcom](https://clawhub.ai/user/samledger67-dotcom)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting operators use this skill to generate rolling cash forecasts from QuickBooks Online data for client advisory, runway monitoring, burn analysis, and scenario-based liquidity planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: QuickBooks Online data, forecast workbooks, and local cache files can contain sensitive client financial information.

Mitigation: Install and run the skill only in a trusted environment with authorized QBO access, protect the .cache/cash-flow-forecast/ files, and choose a secure output directory instead of a shared or cloud-synced Desktop.

Risk: Unpinned dependencies can change workbook generation behavior over time.

Mitigation: Use a pinned dependency environment for openpyxl when generating client-facing reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samledger67-dotcom/skills/cash-flow-forecast)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and Excel workbook output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces CashFlowForecast_{slug}_{YYYY-MM-DD}.xlsx with summary, weekly detail, scenarios, burn rate, assumptions, and CDC log tabs.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
