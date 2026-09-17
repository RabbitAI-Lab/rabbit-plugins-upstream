## Description:

整车厂返利与商务政策核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and dealership operations staff use this skill during monthly close, reconciliation, and inventory review to check OEM rebate and commercial policy tables for arithmetic mismatches, total-row inconsistencies, duplicate rows, blank placeholders, and negative values. The skill reports findings with source row references and withholds conclusions when the input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence marks the release suspicious because the skill steers users toward an external paid installation and purchase flow using an unpinned remote command.

Mitigation: Do not allow an agent to run the embedded npx purchase/install command or follow newly installed onboarding instructions without independent source verification and explicit user consent.

Risk: The free release intentionally omits several rebate-policy checks that are advertised as part of a separate paid product.

Mitigation: Treat results as coverage for the listed free checks only; review the withheld-check list before relying on the output for a complete rebate-policy review.

Risk: The artifact states that it does not interpret commercial-policy terms, tax treatment, period allocation, or source-system data.

Mitigation: Use the output as table-level arithmetic and consistency evidence, and route policy interpretation, tax, accounting-period, or source-system questions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/oem-rebate-policy-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Paid upgrade purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON report with executed checks, withheld checks, missing-input guidance, and row-cited findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free release runs the documented local checks and explicitly lists checks that are not included.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
