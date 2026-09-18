## Description:

集团内部往来对账与抵消核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill during monthly close, reconciliation, and consolidation checks to validate group intercompany reconciliation tables. It recalculates row arithmetic, checks totals, flags duplicate or incomplete rows, and cites source rows for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paid-upgrade path directs users toward an unpinned `npx ... @latest` installer and a purchase flow.

Mitigation: Treat the paid upgrade as a separate trust decision; verify the package source, exact version, permissions, merchant details, and payment terms before allowing an agent to run installers or start a purchase.

Risk: The bundled checker reads supplied reconciliation tables and is written for Chinese-language finance workflows.

Mitigation: Run it locally only on data approved for local processing, and have a qualified reviewer confirm that field mappings and output language match the organization’s accounting workflow.

Risk: The free version omits several business-substance checks, including unresolved balance differences, over-elimination, and unmatched internal transactions.

Mitigation: Use the output as a table arithmetic and completeness check, then perform separate accounting review for consolidation judgments and the omitted checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/group-intercompany-reconciliation-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with source row references and summary counts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; accepts a JSON file or pasted tabular text containing the reconciliation table.]

## Skill Version(s):

1.0.3 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
