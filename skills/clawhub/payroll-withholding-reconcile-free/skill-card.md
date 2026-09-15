## Description:

Checks payroll withholding against individual income tax and social insurance filing tables by recalculating rows, reconciling totals, detecting duplicates and blanks, and citing source lines for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and payroll staff use this free checker during monthly close or reconciliation to compare payroll withholding amounts with individual income tax and social insurance filing figures. It reports row-level arithmetic mismatches, total-row inconsistencies, duplicate people, blanks, and missing filing-side values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional paid upgrade flow can execute an unpinned third-party installer and then follow newly installed skill instructions.

Mitigation: Use the free local checker without the upgrade flow unless the installer source has been reviewed, pinned or verified, and approved by the user before any purchase or installation.

Risk: Payroll inputs may contain sensitive employee compensation and filing data.

Mitigation: Run the checker only in a trusted local environment and avoid sharing payroll records with services or assistants that are not approved for that data.

Risk: The free version omits some checks and does not decide how tax or social insurance should be calculated.

Mitigation: Review the reported checks_not_run and out-of-scope items, then independently validate statutory payroll and filing correctness before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-withholding-reconcile-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay paid upgrade shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local Node.js checks and may return insufficient-input guidance instead of a reconciliation conclusion when required table fields are missing.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
