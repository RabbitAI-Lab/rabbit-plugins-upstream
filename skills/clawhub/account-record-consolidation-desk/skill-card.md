## Description:

Provides account merge guidance and applies account revisions to local records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Account maintenance staff use this skill to set field-preservation guidance and merge an account revision into a local record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream merge receipt may contain sensitive account data in local storage.

Mitigation: Use a dedicated output directory and avoid real sensitive account data unless retaining a local receipt is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wxt-ai/skills/account-record-consolidation-desk)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Text guidance and JSON merge result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream writes a local JSON merge receipt only when given an explicit output directory.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
