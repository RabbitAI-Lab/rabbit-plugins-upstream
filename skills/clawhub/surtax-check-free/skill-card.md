## Description:

A free local checker for VAT surtax worksheets that recalculates row values, verifies totals, detects duplicate or incomplete periods, and cites source line numbers for findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and tax users use this skill to check VAT surtax worksheets for row-level recalculation errors, total mismatches, duplicate periods, and missing required fields. It is intended to support review of supplied worksheet text, not to provide tax advice or determine policy applicability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags a suspicious paid-upgrade prompt that tells an agent to run an unpinned external installer and complete a paid skill installation flow.

Mitigation: Use only the bundled free local checker unless the external installer, onboarding skill, merchant, and payment flow have been separately trusted and reviewed.

Risk: The free checker intentionally withholds several checks, including negative VAT amount detection and abnormal surtax-rate detection.

Mitigation: Treat successful output as limited to the listed executed checks, review the withheld-check list, and do not treat the result as tax advice or policy validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/surtax-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay paid-upgrade shelf referenced by the artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by the artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON result object with findings, summary, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing requirements rather than a positive conclusion.]

## Skill Version(s):

1.0.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
