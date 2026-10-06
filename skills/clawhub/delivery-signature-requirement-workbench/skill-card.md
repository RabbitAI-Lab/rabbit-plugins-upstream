## Description:

Compose a delivery signature section.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff use this skill to create a signature-requirement section for a delivery handoff document from a supplied boolean choice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery target can send generated records to an external endpoint, beyond composing a section locally.

Mitigation: Check and unset CLAWHUB_DELIVERY_ENDPOINT, DELIVERY_ENDPOINT, CLAWHUB_DELIVERY_API_KEY and related delivery variables for local-only use; review any delivery configuration before running.

Risk: Execution saves a delivery record to the selected local directory.

Mitigation: Choose a dedicated writable output directory and review stored records before sharing them.

## Reference(s):

- [Delivery Document Composer on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-signature-requirement-workbench)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON object containing a delivery document section]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a section ID, signature requirement, section type and document count; execution also saves a local record and may return a delivery receipt.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
