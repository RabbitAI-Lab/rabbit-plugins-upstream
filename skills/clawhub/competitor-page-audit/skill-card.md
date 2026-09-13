## Description:

Reviews a primary ASIN and authorized competitor product pages for field completeness, messaging consistency, and review evidence, producing a comparison issue list; it is not for real-time price, sales, inventory, ads, orders, or return-rate conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators use this skill to compare a primary product page with an authorized competitor page, checking listing fields, message consistency, and review-backed evidence before acting on product-page issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is presented as a narrow competitor page audit, but server security evidence says its artifacts expose broader ARI account, review/report, export, monitoring, and paid-analysis capabilities.

Mitigation: Install only when that broader ARI access is intended; for strict page audits, require a narrower package or manual review of actions outside the page_compare/page workflow.

Risk: Some ARI flows can spend credits, adjust confirmation thresholds, create schedules or watches, bind competitors, update workbench state, or export data.

Mitigation: Require explicit user confirmation for paid or persistent changes, especially auto-confirm thresholds, schedules, watches, competitor binding, workbench updates, and exports.

Risk: The skill depends on an ARI API key and can access ARI account data, saved review/report data, and credit-consuming services.

Mitigation: Use a dedicated ARI key, avoid exposing it in chat or reports, and revoke or rotate the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-page-audit)
- [README](artifact/README.md)
- [Operation workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [User guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise text responses, with shell commands or JSON snippets when setup, quoting, or troubleshooting requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, account or credit status, and locally exported files when the user requests supported exports.]

## Skill Version(s):

1.4.8 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
