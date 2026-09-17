## Description:

在建工程转固台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory checks to validate CIP-to-fixed-asset ledger rows. It recalculates formulas, total rows, duplicate projects, blank placeholders, and negative amounts while citing source rows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker embeds and prints a paid upgrade flow that asks an agent to run an unpinned remote installer and begin a purchase.

Mitigation: Install or purchase only after independently verifying the package, source, version, and terms; do not allow an agent to authorize payment or wallet actions on the user's behalf.

Risk: The free version runs only a subset of CIP transfer checks and lists additional checks as paid-version items.

Mitigation: Review the checks not run before relying on results, and perform omitted date, amount, depreciation-start, difference-rate, and post-transfer activity checks separately when needed.

Risk: Ledger conclusions depend on table text with recognizable headers and sufficient row data.

Mitigation: Provide the original table headers and rows, and treat insufficient-input responses as no conclusion rather than as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cip-transfer-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Upgrade purchase instructions referenced by the skill](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands, plus human-readable text or optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; JSON output is available with --json.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
