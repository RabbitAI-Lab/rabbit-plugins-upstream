## Description:

Generates personal or corporate KYC document checklists and reports missing items and completeness scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Individuals and business onboarding teams use this skill to identify missing KYC materials before submitting an application. It is a screening aid, not a compliance determination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad file and web permissions could expose sensitive identity or onboarding information despite the offline-use claim.

Mitigation: Limit access to required local files and disable web access; require explicit approval before any transfer of KYC data.

Risk: A generic checklist and PASS result may not satisfy the requirements of a particular jurisdiction or institution.

Mitigation: Verify requirements against current official guidance and obtain qualified human review before onboarding decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/kyc-checklist-gen)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text checklist or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personal or corporate items, completeness score, missing items, PASS/FAIL status, and exit code.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
