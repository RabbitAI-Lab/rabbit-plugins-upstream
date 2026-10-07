## Description:

Update a section and backlink index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge operations teams use this skill to update a local section and backlink index from a segmented note, removing duplicate sections and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured external delivery can send indexed note content to an unapproved endpoint without a separate confirmation step.

Mitigation: Leave delivery configuration unset for local-only use; approve the endpoint and payload handling before enabling delivery.

Risk: The local index retains note content that may be sensitive.

Mitigation: Use a dedicated output directory and avoid processing sensitive internal notes unless their storage and any configured delivery are approved.

## Reference(s):

- [Knowledge Index Curator on ClawHub](https://clawhub.ai/wxt-ai/skills/knowledge-section-index-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON index update and receipt; local knowledge-index file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes indexed sections, backlinks, deduplication status, and a delivery receipt.]

## Skill Version(s):

1.1.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
