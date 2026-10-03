## Description:

Selects a reviewer group for a request and records the selected group locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and governance teams use this skill to choose a reviewer group for a request and record the group in a local review queue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A locally queued review request could be mistaken for a submission to an external review system.

Mitigation: Use a dedicated output directory, review the local record and receipt, and confirm any external submission separately.

## Reference(s):

- [Request Review Routing Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/request-review-routing-desk)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and, for registration, a local JSON Lines record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selection returns a reviewer group; registration returns the recorded group and a local effect receipt.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
