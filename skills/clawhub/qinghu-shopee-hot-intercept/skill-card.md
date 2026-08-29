## Description:

This skill helps agents research Shopee product opportunities by pulling site and category rankings, checking product details and trend snapshots, assessing follow-selling or differentiated interception strategies, and finding matching 1688 supply sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers and ecommerce analysts use this skill to identify hot or fast-rising products across Shopee regional sites, evaluate sales trends and price bands, and decide whether to follow-sell, differentiate, observe, or abandon a candidate product.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Qinghu tokens for external API calls, so exposed credentials could allow unauthorized market-research requests.

Mitigation: Provide QINGHU_TOKEN or QHKIT_TOKEN only in trusted agent environments and avoid printing or storing tokens in outputs.

Risk: The workflow may consume Qinghu credits when data tools are called.

Mitigation: Require explicit user approval before calling tools, report actual Qinghu credit consumption from the response envelope, and stop when authorization is missing.

Risk: Incorrect parsing of Qinghu responses could treat failed calls as successful because HTTP 200 or a false isError value is not sufficient.

Mitigation: Check protocol errors, result.isError, and the parsed inner response code and success fields before relying on returned data.

Risk: Product follow-selling recommendations can raise brand, patent, import, or marketplace compliance concerns outside the skill's control.

Mitigation: Use the skill for research only and require the user to verify brand authorization, intellectual property, and site-specific compliance before selling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-shopee-hot-intercept)
- [AutoAGC Publisher Profile](https://clawhub.ai/user/autoagc)
- [Qinghu Data API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Concise Markdown responses with strategy recommendations, API call guidance, and exported table files for larger datasets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should label numeric scope by site, accounting date, period, and sample size; datasets with at least 10 records are expected to be exported rather than pasted into chat.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
