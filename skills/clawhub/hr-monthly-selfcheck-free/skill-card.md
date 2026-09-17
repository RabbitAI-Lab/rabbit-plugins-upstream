## Description:

HR Monthly Self-Check Pack (Free) helps finance and HR users run three local checks on segmented payroll, individual income tax withholding, and social insurance or housing fund contribution materials, with findings tied to source lines for offline review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, and HR staff use this skill during monthly close or reconciliation to check segmented payroll, tax withholding, and social insurance or housing fund tables for arithmetic, totals, missing values, duplicates, and cross-table consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes paid-upgrade instructions that ask an agent to install mutable third-party npm code and initiate a separate purchase and skill-install flow.

Mitigation: Do not copy or execute the paid-upgrade prompt unless the package, payment flow, and separate skill are independently vetted; require the user to confirm any wallet authorization or payment.

Risk: The security summary says the skill can falsely report no issues when no checks ran.

Mitigation: Before relying on a no-issue result, confirm the expected sections executed successfully in the output, such as per-check status and section counts.

Risk: The artifact performs deterministic HR/payroll reconciliation checks and does not replace local payroll, tax, filing, audit, or legal judgment.

Mitigation: Use the output as reconciliation support and review findings against source documents and applicable local rules before taking operational or compliance action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/hr-monthly-selfcheck-free)
- [Paid upgrade purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable terminal text or JSON containing findings, per-check status, scope, summary, and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library according to the artifact; insufficient input returns missing-material guidance instead of a finding conclusion.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
