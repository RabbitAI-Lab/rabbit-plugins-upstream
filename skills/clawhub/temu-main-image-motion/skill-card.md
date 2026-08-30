## Description:

Turn one Temu main image into one Temu main image video for the listing video slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to turn an existing Temu listing main image into one short product-motion clip while preserving visible product identity, labels, crop, and background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared broad Beatra device credential.

Mitigation: Install only when that access is acceptable, keep the credential file private, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client can contact Beatra services, upload selected images, and expose generic remote tool calls.

Mitigation: Inspect the image, review the free shot plan, and approve billable video generation only after checking the production card.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with the documented command when reviewed code must remain fixed.

Risk: Transport uncertainty around billable generation could otherwise lead to duplicate work.

Mitigation: Use one opaque client_request_id per approved image and retry only the identical payload when recovery is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/temu-main-image-motion)
- [Beatra skill homepage](https://beatra.ai/skills/temu-main-image-motion)
- [Temu main image motion workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free shot plan before billable work, then one Beatra image-to-video task and delivery report per approved main image.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
