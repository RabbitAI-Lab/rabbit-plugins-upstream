## Description:

Derive field consolidation rules and consolidate account records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and account-maintenance users use this skill to derive account merge guidance from a supplied revision profile and apply that guidance to consolidate account record fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated merge guidance or merged account records may be incorrect for a real business system.

Mitigation: Make explicit stage requests and review generated merged records before applying them to production account data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/account-record-consolidation-desk)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Text and structured object fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces merge_guidance as a string and merge_result as an object with merged_record, changed_fields, and preserved_fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
