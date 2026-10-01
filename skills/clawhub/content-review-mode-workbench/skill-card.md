## Description:

Prepares a field-level content review plan from supplied handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and teams use this skill to select a review lane and prepare a masked preview based on the handling guidance for an item.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive business data could appear in a preview if fields are not masked appropriately.

Mitigation: Review caller-supplied data and specify mask_fields or use restricted handling for sensitive previews.

Risk: A generated review plan could be mistaken for a completed external review or saved in an unsuitable location.

Mitigation: Use a dedicated output directory and review the local CSV before relying on its handling guidance.

## Reference(s):

- [Content Review Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/content-review-mode-workbench)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON review plan and local CSV file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes handling tier, review lane, masked preview, and a local file receipt.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
