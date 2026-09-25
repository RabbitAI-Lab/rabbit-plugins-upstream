## Description:

Derive content handling tiers and build content review plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and operations teams use this skill to set handling guidance for content items and prepare concise review plans from the active workspace inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad phrase routine content handling work could cause an agent to select the skill for content requests where a narrower review workflow is intended.

Mitigation: Before installing, confirm that the skill-selection language matches the agent's allowed content review scope.

Risk: Handling guidance and review plans may be incomplete or misleading if the supplied content_profile or handling_guidance is incomplete.

Mitigation: Review the generated handling guidance or review plan against the source content profile before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/content-review-handling-desk)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [String and structured object fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces handling_guidance as a string or review_plan as an object with handling_tier, review_lane, and masked_preview.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
