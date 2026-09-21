## Description:

Combines set handling guidance for a content item with prepare a content review plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reviewers, and content operations teams use this skill to assign handling guidance to workspace content and prepare a field-level content review plan from that guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incomplete or unsuitable content profiles can lead to handling guidance that does not match the workspace item.

Mitigation: Confirm that the supplied content_profile accurately describes the item and its field inventory before using the resulting guidance.

Risk: The generated review plan may omit fields or checks needed for a specific policy context.

Mitigation: Review the plan before use and adapt it to the applicable content, policy, and release requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/content-review-mode)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text containing handling guidance and a content review plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces handling_guidance from content_profile and review_plan from handling_guidance.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
