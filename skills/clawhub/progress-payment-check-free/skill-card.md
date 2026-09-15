## Description:

Checks construction progress-payment worksheets by recalculating payable amounts, retention deductions, actual payments, totals, duplicate rows, and missing fields, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Construction and engineering finance teams use this skill to check monthly progress-payment tables before approving or reconciling payments. It helps identify arithmetic mismatches, total-row errors, duplicate contract rows, and missing values in the free local checker scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an optional paid-upgrade flow that asks an assistant to run an unpinned installer and initiate payment/install steps.

Mitigation: Use the free local checker without running the paid-upgrade block unless the package, merchant, product, amount, and official source have been separately verified in a trusted environment.

Risk: The free checker intentionally omits some payment-risk checks, including cumulative over-contract checks and out-of-range percentage checks.

Mitigation: Treat results as limited to the listed free checks and review omitted checks separately before relying on the worksheet for payment approval.

Risk: Insufficient or malformed worksheet input can prevent the checker from making a conclusion.

Mitigation: Provide a worksheet with recognizable headers and review missing-input messages instead of treating the absence of findings as approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/progress-payment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with source line numbers and summary fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts worksheet text or JSON containing text.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
