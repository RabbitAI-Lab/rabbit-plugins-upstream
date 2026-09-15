## Description:

Checks export VAT rebate worksheets by recalculating free-tier formulas, verifying totals, detecting duplicate or blank entries, and citing source line numbers for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, tax, and operations staff at exporters use this skill before monthly export VAT rebate filings to check worksheet arithmetic, total rows, duplicate declaration numbers, and missing values. It does not decide tax eligibility, select applicable rebate rates, or provide tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker omits listed paid-tier checks and does not determine tax eligibility, applicable rebate rates, or tax advice.

Mitigation: Review the withheld and out-of-scope checks before relying on results, and have qualified tax staff validate filing decisions.

Risk: The optional paid-upgrade instructions ask an agent to run an unpinned external installer and follow newly downloaded instructions.

Mitigation: Review the SkillPay documentation and package source yourself, avoid running the unpinned @latest installer in sensitive environments, and require explicit human approval for installation and payment steps.

Risk: Rebate worksheets may contain sensitive business or tax data.

Mitigation: Run the checker only in a trusted local environment and avoid sending worksheet data to untrusted agents, shells, or remote services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/export-rebate-check-free)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON containing check status, executed and withheld checks, findings, missing-input details, and source line numbers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on provided worksheet text or JSON input; reports insufficient input instead of producing an unsupported conclusion.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
