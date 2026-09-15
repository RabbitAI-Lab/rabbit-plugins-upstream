## Description:

加班费核算核对（免费） locally checks overtime pay worksheets for arithmetic consistency, totals, duplicate names, blanks, and missing required material, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance users can run this skill before payroll to recalculate overtime worksheet fields, compare subtotals and totals, and identify duplicate or incomplete rows. It is arithmetic assistance for review, not legal advice or payroll approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional paid-upgrade instructions ask an agent to run an unpinned external installer and then follow newly installed skill instructions.

Mitigation: Use the free local checker without the upgrade flow unless the package source and exact version are independently verified and the newly installed instructions are reviewed before execution.

Risk: Overtime findings could be mistaken for legal or payroll approval.

Mitigation: Treat outputs as arithmetic review assistance only, and have payroll, HR, or legal reviewers confirm the final decision.

Risk: Wallet authorization or payment steps could be delegated to an agent during the optional upgrade flow.

Mitigation: Require the user to personally confirm any wallet or payment action through verified official links or QR codes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/overtime-pay-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON report with source-line citations, executed checks, withheld checks, and insufficient-input status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on overtime worksheet text or JSON input; does not approve payroll or provide legal conclusions.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
