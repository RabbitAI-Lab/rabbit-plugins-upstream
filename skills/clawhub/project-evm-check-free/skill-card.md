## Description:

逐项核对挣值分析表的 CV、SV、CPI、SPI、合计行、重复项与空缺项，并在每条结论中引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Project managers, PMO staff, finance reviewers, and delivery engineers use this skill to check copied earned value management worksheet text before monthly progress and cost reporting. It recalculates core EVM formulas and flags missing, duplicate, or inconsistent table entries without making project management recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags documentation that asks an agent to run an unpinned external installer and start a paid skill purchase flow.

Mitigation: Use the free local checker without invoking the paid-edition prompt. Before running any npx installer or authorizing payment, independently verify the SkillPay instructions, package source, exact version, and payment flow.

Risk: The checker does not produce a conclusion when worksheet text lacks required EVM headers or usable values.

Mitigation: Provide copied worksheet text with work package, PV, EV, AC, CV, SV, CPI, and SPI headers, and treat insufficient-input output as no conclusion rather than a clean pass.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-evm-check-free)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON report with cited source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on copied EVM worksheet text; requires recognizable table headers and lists paid-edition checks that are not executed by the free engine.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
