## Description:

Checks batches of patent numbers against PatentMax and prepares a status checklist showing validity, lapse reasons, and estimated expiry years.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent owners, analysts, and legal or procurement teams use this skill to check batches of patent numbers, identify lapsed or pending records, and export a reviewable checklist. For formal legal decisions, confirm results against the official patent register.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers and search terms are sent to an external service, which may expose confidential research or legal strategy.

Mitigation: Use only with data your organization permits sharing with PatentMax/ip930.com.

Risk: The bundled tools include additional patent search and analysis operations that can incur charges.

Mitigation: Review requested operations and estimated costs before running them; get approval for larger or separately billed queries.

Risk: An altered service endpoint could direct searches and credentials to an unintended destination.

Mitigation: Leave PATENTMAX_BASE_URL unset or pin it to the intended PatentMax service.

Risk: Patent status data may lag official records, and expiry years omit special adjustments.

Mitigation: Verify status and expiry against the official patent register before formal legal use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-legal-status)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax tool guide](references/tools.md)
- [PatentMax search workflow](references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [UTF-8 CSV checklist and text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves input order, flags unmatched numbers, and labels expiry years as estimates.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
