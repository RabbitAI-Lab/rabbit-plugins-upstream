## Description:

Turn listing photos into a labeled set of listing room video clips, one room at a time. This listing video pack and real estate room video studio animates each listing photo into a short property video so buyers can preview the living room, bedroom, kitchen, and more as separate room clips. Use it for property room video, listing photo video, real estate listing video, and a labeled room video pack that keeps each space easy to scan. Add optional agent narration files beside the clips, or a talking-head intro and outro when you bring an agent portrait and a short script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate agents and listing teams use this skill to turn inspected listing photos into labeled room-by-room video clips, with optional separate narration files or talking-head intro and outro clips when the user provides the required portrait, script, and rights confirmations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device token stored under ~/.beatra.

Mitigation: Keep the token local, never expose it in chat, logs, command arguments, or environment variables, and revoke the Beatra device connection from the Beatra Console when it is no longer needed.

Risk: The skill uploads user-selected listing media to Beatra for generation.

Mitigation: Inspect and admit only the intended listing photos or authorized portrait files before upload, and avoid submitting sensitive or unrelated media.

Risk: Billable Beatra generation calls can spend credits after user confirmation.

Mitigation: Confirm each paid boundary before submission, use one frozen client_request_id per billable request, and recover uncertain responses only with the identical payload.

Risk: Silent automatic package updates are enabled by default.

Mitigation: In sensitive environments, disable automatic updates with python3 scripts/mcp_client.py update --auto off and use explicit update checks instead.

## Reference(s):

- [ClawHub Listing Room Video Pack](https://clawhub.ai/beatra-ai/skills/listing-room-video-pack)
- [Beatra Listing Room Video Pack](https://beatra.ai/skills/listing-room-video-pack)
- [Listing room video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance with shell commands and generated media artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include labeled room video clips, optional separate narration files, optional talking-head intro or outro clips, and returned task details such as dimensions, duration, usage, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
