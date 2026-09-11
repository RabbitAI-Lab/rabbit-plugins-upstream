## Description:

Turn a written grid-matter list into one grid notice voice clip per labeled cue. This grid matter voice studio records each community grid notice audio and street grid voice from the list the office already wrote, then delivers 8 to 20 grid notice voice pack files. Use it for grid notice clip packs that keep one matter on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and office teams use this skill to turn an already-written grid-matter list into a labeled plan and then generate 8 to 20 grid notice voice clips, with optional authorized voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra Device Token grants broad media, artifact, task, and wallet capabilities for this shared connection.

Mitigation: Install only after accepting that scope, keep the token confined to the documented credential file, use an account with limited funds, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client silently replaces package-owned files by default when a newer verified release is available.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before use when silent replacement is not acceptable, or use `update --check` to inspect availability without replacing files.

Risk: Paid clone and speech requests can spend credits, and careless retries can create duplicate work.

Mitigation: Require the documented six-field paid-stage cards, read live pricing before submission, use one opaque `client_request_id` per paid request, and recover uncertain responses only with byte-identical arguments.

Risk: Voice cloning or local file upload can send sensitive or unauthorized voice samples to Beatra.

Mitigation: Clone only when the user confirms likeness and voice rights, inspect the sample first, and upload only files the user explicitly intends to send through the bundled client.

## Reference(s):

- [Grid notice voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/grid-notice-voice)
- [Beatra skill homepage](https://beatra.ai/skills/grid-notice-voice)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance, audio files]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands; generated speech tasks return audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one labeled clip per written grid-matter cue, usually 8 to 20 clips, and uses live task, billing, and artifact fields when reporting generated results.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
