## Description:

Checks Chinese-language government and public-information disclosures for mentions of decision basis, responsible department, deadline, appeal channels, and data source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

Compliance teams and developers use this Chinese-language checklist to find potentially missing fields in government or public-information disclosure drafts. Human reviewers must verify the content and applicable current requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keyword matches can miss substantive gaps or incorrectly suggest a disclosure is complete.

Mitigation: Review each field and confirm legal requirements against current official sources; do not treat results as legal advice.

Risk: Network-enabled tools could expose sensitive disclosure drafts.

Mitigation: Keep drafts local and approve network access on business data only when needed for current official references.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/gov-disclosure-check)
- [Publisher's LGD overview](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies missing field categories and returns exit status 0 when none are missing, 1 when fields are missing, or 2 for usage errors.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
