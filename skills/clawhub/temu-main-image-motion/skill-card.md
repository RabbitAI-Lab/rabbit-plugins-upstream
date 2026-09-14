## Description:

Turn one Temu main image into a short product-motion video for a Temu listing video slot while preserving the supplied photo as the first frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, commerce operators, and their agents use this skill to turn a supplied Temu main listing image into one short product-motion clip. The workflow supports pre-generation shot planning, live model admission, billing confirmation, task polling, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a persistent Beatra bearer token with broad account authority for media generation, wallet spending, task access, uploads, and cancellation.

Mitigation: Review the requested authorization before installation, keep the credential file private, and revoke the device from the Beatra Console when the shared credential should no longer be active.

Risk: Selected local images are uploaded to Beatra to produce the requested video clip.

Mitigation: Upload only images the seller has provided for this task, inspect files before upload, and avoid sending unrelated or sensitive media.

Risk: Executable package files silently self-update by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when strict change control is required, and use the explicit update check command before updating.

Risk: Billable video generation can duplicate charges if an uncertain request is retried with changed inputs or a new request identity.

Mitigation: Use one opaque `client_request_id` per approved image and retry only the identical payload with the same ID after transport uncertainty.

## Reference(s):

- [Temu main image motion workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/temu-main-image-motion)
- [Beatra skill homepage](https://beatra.ai/skills/temu-main-image-motion)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate image upload and Beatra MCP calls through bundled scripts after user confirmation; generated video artifacts are returned by Beatra task results.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
