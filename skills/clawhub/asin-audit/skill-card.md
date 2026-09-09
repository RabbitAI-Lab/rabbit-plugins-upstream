## Description:

Amazon ASIN 运营体检 combines product-detail and review evidence to identify issues, supporting evidence, and operations priorities for a single Amazon ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and sellers use this skill to audit a single ASIN, combining product details and review evidence into prioritized operational actions. It is not intended for ad bidding, inventory, profit, or order accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an ARI account key to run paid analyses and may change monitoring or confirmation settings.

Mitigation: Keep auto-confirm off when per-action approval is required, review quoted costs before confirming paid actions, and verify monitoring or competitor setup requests before agreeing.

Risk: Exports and account operations can expose ARI account data or write files to user-selected paths.

Mitigation: Choose export paths deliberately, avoid sharing API keys in chat or reports, and review generated files before redistribution.

Risk: A custom ARI API base URL could redirect authenticated requests away from the official service.

Mitigation: Use the default ARI endpoint unless a trusted HTTPS custom endpoint is explicitly intended and reviewed.

Risk: Operational recommendations may be misleading when review samples, time windows, or product data are incomplete.

Mitigation: Treat the output as decision support, preserve stated data limits, and validate important business decisions against additional evidence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/asin-audit)
- [README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [Amazon ASIN 运营体检 专属运营工作流](artifact/references/operation-workflow.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise conversational guidance, with shell commands or JSON details for advanced CLI workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN/site scope, sample size, analysis window, report ID, report URL, credits used, and current balance when returned by ARI.]

## Skill Version(s):

1.4.8 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
