## Description:

进口税费核算核对（免费版）本地复算进口税费计算表中的关税、消费税、增值税、税费合计和合计行，并用原文行号标注发现的问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External importers, freight forwarders, customs teams, and finance teams use this skill before payment to recalculate import-duty worksheets and check arithmetic, totals, duplicate rows, and missing fields. It supports review by citing source line numbers and by declining to conclude when required material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review marks the release suspicious because the skill includes optional agent-assisted dependency installation, external instructions, and a paid purchase flow.

Mitigation: Use the bundled free local checker without following paid-upgrade automation; do not run the npx purchase installer or authorize purchases unless the user independently trusts SkillPay, the package publisher, the exact resolved package version, and the newly installed skill.

Risk: The free checker omits tax-rate range checks, non-positive dutiable value checks, negative tax checks, and comprehensive tax-burden anomaly checks.

Mitigation: Treat the output as a scoped worksheet arithmetic review and supplement it with independent checks for omitted conditions before relying on the result.

Risk: The engine does not determine customs tariff classification, applicable tax rates, customs acceptance of declared value, compound or quantity-based taxes, exchange-rate conversion, or tax advice.

Mitigation: Have a qualified customs or tax reviewer validate classification, rates, declared value, special taxes, and exchange-rate treatment separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/import-duty-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown guidance with optional structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; --json mode emits status, executed checks, withheld checks, summary totals, and findings.]

## Skill Version(s):

1.0.15 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
