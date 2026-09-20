## Description:

物流仓储与操作费结算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and supply-chain reconciliation staff use this skill before payment to check third-party warehouse storage and handling settlement tables for arithmetic mismatches, duplicate rows, blanks, placeholders, and negative amounts. It reports findings with source-line evidence and withholds conclusions when the input does not contain enough table data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may process sensitive billing or logistics settlement data.

Mitigation: Run the skill only in an environment approved for that data and avoid adding unnecessary confidential fields to the input text.

Risk: The documentation's usage-statistics wording does not match the inspected code.

Mitigation: Review the installed artifact and network policy before deployment if telemetry behavior matters for the environment.

Risk: The free version intentionally omits some checks and does not assess whether warehouse pricing policies are commercially reasonable.

Mitigation: Use the findings as arithmetic and completeness checks, then review contract pricing, policy reasonableness, taxes, invoices, and payment terms separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/logistics-storage-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON check report with source-line evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local Node.js checks on user-provided Chinese-language logistics settlement table text; insufficient input returns missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.54 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
