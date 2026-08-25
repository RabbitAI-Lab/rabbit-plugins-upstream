## Description:

Create multilingual voice-over audio from prepared scripts for videos, product launches, e-learning, training libraries, creator content, and international campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, localization teams, and training teams use this skill to plan, approve, synthesize, recover, and deliver multilingual voice-over narration by locale and segment using Beatra text-to-speech tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization stored locally for remote MCP operations.

Mitigation: Install only when the user trusts Beatra, keep the credential private, watch paid render approvals closely, and revoke the device authorization from the Beatra Console when the skill is no longer needed.

Risk: The bundled client can silently update installed package code from Beatra's package channel.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when that update posture is not acceptable, and use `python3 scripts/mcp_client.py update --check` to inspect available updates.

Risk: Each approved speech synthesis cell is paid work, and transport uncertainty can otherwise lead to duplicate submissions.

Mitigation: Confirm the full paid scope once, use one stable `client_request_id` per approved cell, poll existing task IDs before retrying, and retry uncertain submissions only with identical arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-multilingual-dubbing)
- [Beatra skill homepage](https://beatra.ai/skills/ai-multilingual-dubbing)
- [Matrix design](references/matrix-design.md)
- [Locale readiness and quality](references/locale-readiness-and-quality.md)
- [Recovery and delivery](references/recovery-and-delivery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, JSON MCP payloads, task status summaries, and delivered audio URLs with metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid Beatra speech synthesis tasks after explicit user approval and reports task identity, billing result, artifact details, MIME type, size, sample rate when returned, and duration.]

## Skill Version(s):

0.1.7 (source: server release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
