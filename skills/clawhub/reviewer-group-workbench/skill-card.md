## Description:

Register a request reviewer group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operational reviewers use this skill to register the reviewer group selected for a request handoff and return a concise recorded_group object.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied reviewer_group may be inappropriate for the current request handoff.

Mitigation: Confirm the reviewer_group value matches the current request before using the recorded_group result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/reviewer-group-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON object in the recorded_group field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes review_request_id, reviewer_group, queue_name, and due_hours.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
