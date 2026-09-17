## Description:

本技能在本地核对外币结算核对表，复算记账本位币、结算本位币、汇兑损益、已收本位币、合计行、重复单据和空白占位字段，并为每条结论标注原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users use this skill to check Chinese-language FX settlement worksheets before month-end review or reconciliation. It helps identify arithmetic mismatches, reversed FX gain/loss direction, inconsistent received amounts, duplicated document numbers, and missing required fields when the worksheet text includes recognizable headers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes a paid-upgrade section and CLI purchase/install instructions for a separate product.

Mitigation: Use the skill only for local FX worksheet checking unless the package, source, version, and payment flow have been independently verified.

Risk: The paid-upgrade instructions include an unpinned `npx ...@latest` command and ask the agent to load newly installed skill instructions.

Mitigation: Do not let an agent run the unpinned command, load new skill instructions, or initiate purchase/install steps without explicit independent review and user confirmation.

Risk: The free checker omits several checks and does not provide accounting or tax opinions.

Mitigation: Treat clean results as arithmetic consistency checks only, and separately review accounting policy, tax treatment, period-end remeasurement, hedging, and any withheld checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/fx-settlement-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON containing findings, summaries, executed checks, withheld checks, and insufficiency notices.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers. The free version runs locally and lists checks that were not executed.]

## Skill Version(s):

1.0.11 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
