## Description:

Turn user-supplied policy renewal dates and authorized stills into short insurance renewal reminder talking clips, one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance advisors and wealth educators use this skill to create short renewal reminder talking clips from supplied renewal schedules and authorized stills, with staged approval before paid clone, speech, or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared full-scope Beatra device connection for media generation, uploads, wallet spending, task reads, and cancellation.

Mitigation: Install only where that broad Beatra account scope is acceptable, keep the device token private, and reconnect with the documented authorization helper only when the user explicitly approves.

Risk: The bundled client performs default silent package update checks and can install a newer verified package release.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before normal use when local review or change control is required.

Risk: The workflow uploads local stills and can use cloned voices, which may involve private media, likeness, and voice rights.

Mitigation: Use only authorized stills and voice samples, inspect media before upload, and do not treat file access as consent.

Risk: Clone, speech, and video stages are paid remote operations where retries or changed inputs can create additional billable tasks.

Mitigation: Show stage-specific approval cards with live prices, use unique `client_request_id` values, and retry only byte-identical requests when delivery is uncertain.

Risk: Uninstall behavior can affect shared Beatra connection state used by other Beatra skills.

Mitigation: Use the bundled uninstall decision script and remove only the package directory it identifies; do not manually delete shared `~/.beatra` state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/insurance-renew-talking)
- [Beatra Skill Homepage](https://beatra.ai/skills/insurance-renew-talking)
- [Beatra MCP Endpoint](https://mcp.beatra.ai/mcp)
- [Renewal reminder talking-clip workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown planning and approval text with JSON payload examples, shell commands, and generated media artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 2-8 independent 2-15s talking clips; reports MIME type, duration, size, task ID, usage, and net charged credits when returned.]

## Skill Version(s):

0.1.1 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
