## Description:

Turn confirmed booking facts into one booking confirmation voice clip per labeled notice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Shop staff and agents use this skill to turn confirmed booking, reschedule, cancellation, reminder, and related notice facts into labeled voice clips for customer communications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device token authorizes broad media, artifact, wallet, voice, and task permissions beyond the narrow booking-voice task.

Mitigation: Review the requested access before installation, keep the token only in the documented local credential file, and disconnect or uninstall the package when it is no longer needed.

Risk: Package-owned code updates are silent by default.

Mitigation: Disable automatic update checks with `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable, and use the documented update check before re-enabling them.

Risk: Voice clone and speech synthesis steps can spend account credits or duplicate work if retried with changed inputs.

Mitigation: Require an explicit cost card before each paid stage, use one opaque `client_request_id` per paid request, and recover uncertain submissions only with byte-identical arguments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/demo-booking-confirm)
- [Beatra Skill Homepage](https://beatra.ai/skills/demo-booking-confirm)
- [Booking Confirmation Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Bundled MCP Client Diagnostics](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces labeled booking-notice slot lists and guides optional paid voice clone and speech synthesis tasks; intended clip count is usually 8 to 20.]

## Skill Version(s):

0.1.3 (source: server evidence release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
