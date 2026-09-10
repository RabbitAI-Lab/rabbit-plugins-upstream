## Description:

把 Amazon 评论中的质量、包装和说明问题整理为供应商沟通要点、证据与验收问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to turn review evidence into supplier feedback, product-quality discussion points, and acceptance questions. It is not intended to contact suppliers, place purchase orders, make contract decisions, or determine legal responsibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence flags that the skill exposes broader ARI seller-operations behavior than the supplier-feedback description suggests, including paid operations, monitoring, exports, and account-setting changes.

Mitigation: Install only when that broader ARI seller-operations scope is expected; review billing auto-confirm settings, monitoring and schedule changes, export destinations, and custom API endpoint settings before use.

Risk: Paid collection or analysis may deduct credits when confirmed or when account auto-confirm rules apply.

Mitigation: Use quote-only flows when seeking pricing, confirm credit costs before paid runs, and check recent reports or task status before retrying interrupted paid operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/supplier-feedback)
- [README](artifact/README.md)
- [使用说明](artifact/使用说明.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Supplier feedback operation workflow](artifact/references/operation-workflow.md)
- [ARI API keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI billing](https://ari.funewa.com/zh/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Chinese natural-language responses, Markdown reports, structured JSON command results, and optional CSV, Markdown, or HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Some ARI collection, analysis, monitoring, export, and account-setting workflows can affect credits or saved account state.]

## Skill Version(s):

1.4.8 (source: server release metadata, artifact frontmatter, _meta.json, CHANGELOG.md, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
