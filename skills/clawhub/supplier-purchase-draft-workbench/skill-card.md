## Description:

Creates a purchase draft from structured supplier terms, saving a local record and optionally submitting it to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement staff use this skill to turn structured supplier terms into a purchase draft for sourcing or renewal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured external endpoint can receive purchase-draft data without strong scoping or confirmation.

Mitigation: Leave CLAWHUB_DELIVERY_ENDPOINT and --delivery-config unset for local-only use; review the endpoint, API key, and output directory before using real procurement data.

## Reference(s):

- [Purchase Draft Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON purchase draft result and local purchase record; optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a draft identifier, status, supplier identifier, and summary.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
