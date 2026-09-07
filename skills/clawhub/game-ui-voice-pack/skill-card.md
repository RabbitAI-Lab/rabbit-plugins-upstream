## Description:

Turn written game UI lines into one game voiceover clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External game studios and developers use this skill to turn already-written game interface cues into a labeled set of voice clips. It helps plan, submit, poll, review, and recover Beatra text-to-speech or approved voice-clone jobs for 8 to 20 UI cues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authorization, including media generation, artifact access, wallet spending, task reads, and task cancellation.

Mitigation: Install only for Beatra accounts where that scope is acceptable, keep the device token private, and revoke the connected device from the Beatra Console when the skill is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Review the package before use and disable silent updates with `python3 scripts/mcp_client.py update --auto off` when update control is required.

Risk: Paid clone and speech calls can spend account credits and may duplicate cost if retried with changed arguments.

Mitigation: Use one opaque `client_request_id` per paid request, retry uncertain delivery only with byte-identical arguments, and read Beatra billing fields before reporting final charges.

Risk: Voice cloning can create likeness and consent concerns.

Mitigation: Use cloning only when the user supplies an authorized sample and explicit rights, and keep catalog voices as the default when those rights are missing.

## Reference(s):

- [Game UI voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Audio artifacts]

**Output Format:** [Markdown with inline JSON and bash examples, plus generated audio artifact references when tasks succeed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one clip per labeled UI cue, tracks paid task IDs and billing fields, and reports only returned audio metadata.]

## Skill Version(s):

0.1.2 (source: server release evidence, manifest.json, and bundled script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
