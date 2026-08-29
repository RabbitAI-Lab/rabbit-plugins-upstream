## Description:

Turn a written grid-matter list into one grid notice voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and office staff use this skill to turn an already-written grid-matter list into a labeled pack of 8 to 20 short notice voice clips. It supports catalog voices or explicitly authorized staff voice cloning while preserving one matter per clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device authorization with broad media, task, artifact, voice, and wallet scopes.

Mitigation: Install only on a Beatra account and machine intended for this work, and disconnect through the bundled uninstall flow or Beatra Console when access is no longer needed.

Risk: The bundled client stores a Beatra device credential locally.

Mitigation: Keep the local Beatra state private, do not expose tokens in chat, logs, command arguments, or diffs, and use the bundled authorization helper for recovery.

Risk: The bundled client can silently auto-update package files.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` or run `python3 scripts/mcp_client.py update --check` before accepting updates.

Risk: Paid speech or clone requests can create duplicate charges if retried with changed arguments or a new request identity after transport uncertainty.

Mitigation: Use one opaque `client_request_id` per billable request, poll returned task IDs, and retry only byte-identical arguments with the same request identity.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/grid-notice-voice)
- [Beatra skill homepage](https://beatra.ai/skills/grid-notice-voice)
- [Grid notice voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Audio files]

**Output Format:** [Markdown with inline JSON and shell commands; Beatra task results include audio artifact metadata and files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 spoken clips from supplied written notices; paid clone and speech stages require explicit confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
