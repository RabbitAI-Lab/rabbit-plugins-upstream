## Description:

Turn user-supplied merchant inspection notices and authorized stills into one talking video clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External market-supervision offices use this skill to turn supplied merchant notices and authorized still images into short talking-clip packs. Agents use it to plan slots, confirm paid Beatra stages, submit speech and video jobs, and deliver one independent clip per still.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device authorization with broad Beatra capabilities.

Mitigation: Review the Beatra account and device access before use, keep the credential private, and revoke or uninstall the connection when it is no longer needed.

Risk: Silent package updates are enabled by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` before use if automatic package updates are not acceptable for the deployment.

Risk: Media upload, voice cloning, speech synthesis, and video animation can process sensitive or unauthorized likeness and voice material.

Mitigation: Provide only media and voice samples that the user is authorized to upload, clone, synthesize, or animate, and confirm rights before paid stages.

Risk: Clone, speech, and video stages are paid Beatra operations and duplicate submissions can consume credits.

Mitigation: Confirm live pricing before each paid stage, use one opaque `client_request_id` per logical request, and retry only unchanged uncertain requests with the same identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/market-inspect-talking)
- [Beatra Skill Homepage](https://beatra.ai/skills/market-inspect-talking)
- [Merchant Notice Talking-Clip Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; completed Beatra tasks can return audio or video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one slot per still, uses explicit request identities for paid stages, and delivers independent 2-15 second clips without stitching.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
