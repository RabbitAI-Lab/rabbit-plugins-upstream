## Description:

Prepare a content review plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and agents use supplied handling guidance to prepare a field-level review plan, choose a review lane, and create a masked preview of workspace content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When external delivery is configured, review-plan data and a local artifact path may be sent outside the workspace.

Mitigation: Leave delivery settings unset for local-only planning; otherwise require explicit approval and an allowlisted destination before running.

## Reference(s):

- [Content Review Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/content-review-mode-workbench)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON review plan and local artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes handling tier, review lane, and masked preview; configured delivery returns a receipt.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
