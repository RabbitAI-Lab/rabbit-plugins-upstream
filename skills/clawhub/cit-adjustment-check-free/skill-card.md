## Description:

企业所得税纳税调整表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax practitioners use this skill before annual corporate income tax filing to check a corporate income tax adjustment table for arithmetic consistency, duplicate or blank items, and negative adjustment amounts. It reports missing input rather than issuing conclusions when the supplied table is insufficient.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill points users toward an external paid-upgrade flow that uses an unpinned installer.

Mitigation: Independently verify the package, merchant, product, and payment flow before allowing an agent to run the installer or start a purchase.

Risk: The free edition intentionally omits five checks and does not determine whether tax-law positions or preferential tax rates are valid.

Mitigation: Use the output as an arithmetic and cross-footing screen, then review withheld checks, out-of-scope tax issues, and filing decisions with authoritative tax guidance or a qualified reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cit-adjustment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Complete edition purchase instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or JSON with findings, executed checks, omitted checks, scope, and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs six free checks locally; insufficient input returns missing requirements without drawing a conclusion.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
