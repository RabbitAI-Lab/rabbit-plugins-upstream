## Description:

Creates short talking video clips from user-supplied wealth product factsheet points and authorized stills, with one 2 to 15 second clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and educators use this skill to turn supplied product factsheet points and authorized stills into short per-still talking clips. It guides consent, cost confirmation, task submission, polling, and delivery for Beatra speech and video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra device authorization for media generation, uploads, wallet spend, task reads, and cancellation.

Mitigation: Authorize only when the Beatra account permissions and billing exposure are acceptable; revoke access from the Beatra Console or through the bundled uninstall flow when no longer needed.

Risk: Selected factsheets, stills, and optional voice samples may be uploaded to Beatra for generation.

Mitigation: Use only materials the user can authorize, and confirm likeness and voice rights before cloning, speech synthesis, or video generation.

Risk: Silent package updates are enabled by default and can replace local package code.

Mitigation: Review the documented update controls and disable automatic checks for this installation with `python3 scripts/mcp_client.py update --auto off` when that posture is required.

Risk: Paid clone, speech, and video tasks can consume credits, and uncertain transport responses can otherwise lead to duplicate work.

Mitigation: Show the stage-specific approval card before paid work, use opaque `client_request_id` values, poll existing tasks, and retry only byte-identical requests with the same request identity.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/wealth-product-talking)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-product-talking)
- [Factsheet talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request payloads; generated audio and video artifacts are returned by Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list before paid work and one talking video clip per approved still or segment; clips are not stitched.]

## Skill Version(s):

0.1.3 (source: server release metadata, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
