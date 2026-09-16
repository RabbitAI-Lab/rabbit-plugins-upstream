## Description:

门店营收上报表逐项核对，每条结论都带原文行号，不需要付款，也不需要注册。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and operations teams use this skill to check copied store revenue report tables for channel-total arithmetic, reported-revenue differences, total-row mismatches, duplicate store/date rows, and blank or placeholder fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes optional guidance that directs users toward an external paid install and purchase flow beyond the free local checker.

Mitigation: Use the free local checker only unless a human independently verifies the external package, publisher, version, and payment terms in a separate, user-controlled environment.

Risk: The checker covers only the free checks and omits several paid-edition checks, so a clean result is limited to the stated reconciliation rules.

Mitigation: Treat results as table arithmetic and completeness checks, not as an audit conclusion or proof that all revenue was captured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-sales-report-check-free)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON findings with source line references, summary totals, executed checks, withheld checks, and advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on tabular text input and reports insufficient input instead of making unsupported conclusions.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
