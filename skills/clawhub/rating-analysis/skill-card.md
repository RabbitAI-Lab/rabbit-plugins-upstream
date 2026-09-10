## Description:

Analyzes an Amazon ASIN's star-rating structure, rating distribution over time, low-rating concentration, and likely causes of rating decline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to diagnose ASIN rating structure, summarize review evidence and trends, and decide whether rating drops point to batch issues or persistent product problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an ARI account key for paid analyses, account checks, exports, monitoring setup, and auto-confirm spending preferences.

Mitigation: Review before installing, turn auto-confirm off when per-action approval is required, and approve credit-consuming actions only after checking the quoted cost and account balance.

Risk: Broad requests such as analyzing a product can trigger wider review-operations workflows and credit use.

Mitigation: Specify the ASIN, Amazon marketplace, analysis scope, and whether the request is quote-only before execution.

Risk: Persistent monitoring can create ongoing collection costs.

Mitigation: Require explicit confirmation of the schedule and returned cost note before enabling weekly or daily monitoring; use manual collection when ongoing monitoring is not needed.

Risk: Interrupted paid commands may already have charged credits or generated a report.

Mitigation: Check existing reports or the original request status before retrying any confirmed paid command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/rating-analysis)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](artifact/README.md)
- [Usage Guide](artifact/使用说明.md)
- [ARI API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with optional shell commands, report links, and export references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis, collection, monitoring, and export actions follow ARI account credit and confirmation rules.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
