## Description:

水电抄表与账单核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, property operations, park operations, and factory operations users can run this local checker during monthly utility close, reconciliation, or inventory review. It verifies table arithmetic for meter usage, receivables, totals, duplicate meter-period rows, missing required fields, placeholders, and negative readings or amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact documentation includes an optional paid-upgrade flow that asks an agent to run an unpinned external installer with `npx ... @latest`.

Mitigation: Use the bundled free checker locally for reconciliation unless the user explicitly wants the paid purchase/install workflow and has independently verified the SkillPay package and payment steps.

Risk: The free checker intentionally omits several checks, including reverse-reading detection, bill-versus-receivable mismatch prompts, price-reference checks, high-usage prompts, and meter-replacement carryover prompts.

Mitigation: Treat results as coverage for the listed free checks only, and review `checks_not_run` before relying on the output for a full utility billing audit.

Risk: The checker does not determine local water or electricity tariff correctness, inspect physical meters, handle penalties or refunds, allocate master-meter losses, or parse spreadsheet files directly.

Mitigation: Provide text with the required table headers, compare tariffs against contracts or utility bills separately, and keep excluded business judgments outside this skill's conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-meter-reading-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact-declared paid upgrade instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [Artifact-declared SkillPay storefront](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable terminal text or JSON with findings, scope, summary, checks not run, and limitations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line context when checks run; insufficient input produces missing-field guidance instead of a positive or negative reconciliation conclusion.]

## Skill Version(s):

1.0.5 (source: evidence.json release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
