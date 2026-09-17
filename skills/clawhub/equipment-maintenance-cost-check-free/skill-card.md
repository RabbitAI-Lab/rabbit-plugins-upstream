## Description:

Checks equipment maintenance and spare-part issue ledgers for labor-cost math, spare-part amount math, monthly budget rollups, total-row reconciliation, duplicate rows, missing key fields, negative values, and possible duplicate charging, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Manufacturing, property operations, logistics, and finance teams can use this skill before monthly close to check equipment maintenance and spare-part ledgers for arithmetic, reconciliation, duplicate-entry, missing-field, and negative-value issues. The free edition does not determine warranty entitlement, outsourced-repair overrun justification, or special accounting treatments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release suspicious because it includes AI-directed paid-upgrade instructions that install unpinned remote payment tooling.

Mitigation: Review the paid-upgrade path separately, do not run unpinned `npx ... @latest` payment installation commands automatically, and require explicit user confirmation before any purchase or wallet authorization.

Risk: The artifact is a Chinese-language local ledger checker, which may be hard for reviewers or operators who cannot read Chinese to audit confidently.

Mitigation: Have a Chinese-reading reviewer verify the user-facing workflow, scope limits, and payment-related guidance before deployment.

Risk: The free edition intentionally omits warranty-charge, outsourced-repair overrun, over-issue, and prioritized recovery-list checks.

Mitigation: Communicate omitted checks in the result and avoid presenting the free-edition output as a complete maintenance-cost recovery analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/equipment-maintenance-cost-check-free)
- [Purchase and installation guidance referenced by the artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by the artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Analysis, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, omitted checks, cited line numbers, findings, and remediation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against text or JSON ledger input; insufficient input is reported without producing a false no-issues conclusion.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
