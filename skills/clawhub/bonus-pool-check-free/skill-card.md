## Description:

Checks year-end bonus allocation and individual income tax worksheets by recalculating allocation, net bonus, annual one-time bonus tax, totals, duplicate people, and blank placeholders, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, finance, and HR operators use this skill to validate year-end bonus pool spreadsheets exported or pasted as text before payroll finalization. It recalculates declared bonus allocation, net bonus, annual one-time bonus tax, totals, duplicates, and missing fields without treating incomplete material as clean.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security summary flags that documentation and default output steer users toward an external paid install and purchase flow using an unpinned installer.

Mitigation: Use the local checker path for normal use; independently verify the package and source before running any installer or purchase flow, and require the user to approve each install and payment step.

Risk: The skill processes payroll and tax-related data, which can be sensitive and authorization-bound.

Mitigation: Use it only with payroll data the operator is authorized to process, and prefer local execution so materials are not pasted into external services.

Risk: The free edition omits checks for invalid tax-method values, negative tax, non-positive performance coefficients, and unusually high tax relative to gross bonus.

Mitigation: Treat successful results as limited to the listed free checks and separately review withheld or out-of-scope conditions before payroll decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/bonus-pool-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable terminal output or JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include severity, category, source line, message, advice, summary totals, executed checks, withheld checks, and out-of-scope checks.]

## Skill Version(s):

1.0.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
