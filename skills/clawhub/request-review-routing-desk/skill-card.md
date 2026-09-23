## Description:

Select reviewer groups and register request review records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Governance and operations teams use this skill to select an appropriate reviewer group for a request and record that group for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A deployment could bind the registration step to a real ticketing or governance system with the wrong write target.

Mitigation: Before production use, confirm the external registration tool writes only to the intended review queue and uses user-supplied request data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/request-review-routing-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [String for reviewer group selection and JSON object for recorded group registration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces stage-specific output fields: reviewer_group or recorded_group.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
