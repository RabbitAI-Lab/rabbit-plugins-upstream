## Description:

A free payroll pre-release checking skill that verifies net pay arithmetic, control totals, duplicate people, and blank or placeholder amounts, with line-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR, payroll, finance, and accounting users can use this skill before salary disbursement to check pasted payroll table text for arithmetic mismatches, incorrect totals, duplicate employee rows, and incomplete values. It supports local review of payroll evidence but does not determine what any employee should be paid or provide tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes paid-upgrade instructions that ask an assistant to run an unpinned external installer.

Mitigation: Review the SkillPay guide, package name, version, merchant, product, and payment step manually; avoid `@latest` installers in sensitive environments.

Risk: Payroll tables can contain sensitive employee compensation data.

Mitigation: Run the free checker locally, avoid sending payroll inputs to unrelated services, and handle input files under the organization's payroll data controls.

Risk: The free checker covers only four payroll checks and can miss issues outside that scope.

Mitigation: Treat clean results as limited to net pay arithmetic, total rows, duplicate people, and blanks or placeholders; use separate review for taxes, pay entitlement, benefit bases, and bank disbursement totals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-check-free)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text or JSON payroll check results with line-cited findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a sample input, JSON input, or pasted payroll table text with headers.]

## Skill Version(s):

1.0.4 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
