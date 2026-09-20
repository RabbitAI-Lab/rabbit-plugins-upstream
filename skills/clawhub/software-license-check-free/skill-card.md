## Description:

软件许可与云资源台账逐项核对，复算年费用、月均费用和账期月数，检查超装、重复行、合计、空缺负值与日期倒挂，并为每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

IT asset administrators, finance teams, and operations staff use this skill to check software license and cloud resource ledgers before quarterly budgeting, renewal decisions, and license-expiry reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Software license and cloud-cost ledgers may contain sensitive business data.

Mitigation: Run the checker in an approved local environment and confirm telemetry disclosure requirements before use; the security evidence says ledger material is processed locally and is not sent over the network.

Risk: The skill checks table arithmetic and consistency, but does not determine vendor-specific software authorization terms or provide legal compliance advice.

Mitigation: Treat findings as ledger review signals and confirm licensing rights, contract terms, and compliance obligations against source contracts or legal review.

Risk: Unsupported or incomplete input can produce an insufficient-input response rather than a substantive conclusion.

Mitigation: Provide a complete text or JSON ledger with the expected headers and export spreadsheets before running the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/software-license-check-free)
- [Sample ledger input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON with line-cited ledger findings and missing-input guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code; insufficient input returns missing fields instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.42 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
