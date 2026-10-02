## Description:

Prepare supplier purchasing terms and create a purchase draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement staff use the skill to turn supplied supplier data into purchasing terms and create a local purchase draft from those terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream run creates or updates a local SQLite draft database.

Mitigation: Supply a dedicated output directory and review local drafts before treating them as purchasing actions; no purchasing service is contacted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/procurement-draft-desk)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON supplier terms and purchase draft details; local draft database for downstream runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream returns purchasing terms without saving a business artifact; downstream creates or updates a local draft database and does not contact a purchasing service.]

## Skill Version(s):

3.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
