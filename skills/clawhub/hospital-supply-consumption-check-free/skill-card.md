## Description:

药品耗材进销存与科室领用核对表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并让每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, pharmacy, and supply staff use this skill during monthly close, reconciliation, or inventory review to check hospital medicine and consumable movement tables. It helps identify arithmetic mismatches, total-row discrepancies, duplicate rows, blanks, placeholders, and negative quantity or amount values using the provided table text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented paid upgrade path can lead users to install mutable third-party tooling and initiate a purchase flow.

Mitigation: Use the free checker only for local reconciliation unless the publisher, package, version, source, and SkillPay process have been independently trusted; require the human user to confirm any wallet authorization or payment.

Risk: The free checker intentionally omits several checks, including negative ending inventory, outflow exceeding available stock, and price mismatch checks.

Mitigation: Treat results as limited to the executed free checks and review the listed checks_not_run before relying on the output for close, audit, or compliance decisions.

Risk: Insufficient or malformed input can prevent the checker from producing a conclusion.

Mitigation: Provide the full table with required headers and, when automating, prefer --json and handle insufficient_input separately from a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/hospital-supply-consumption-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON result objects with findings, scope, summary, and source-line details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts sample input or a user-provided JSON/text file and can emit machine-readable JSON with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
