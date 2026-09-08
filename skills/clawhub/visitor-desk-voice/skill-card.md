## Description:

Turn a written visitor reception script into labeled visitor-reception voice clips, producing an 8 to 20 clip visitor desk voice pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Front desk teams and agents use this skill to turn existing reception scripts into labeled visitor greeting, check-in, escort, safety, policy, and farewell voice clips. It can also guide an authorized staff voice clone before speech generation when the user has the required likeness and voice rights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses broad account, update, telemetry, and shared-credential capabilities beyond basic visitor-desk voice generation.

Mitigation: Review the package before installing in sensitive or managed environments and install it only where those Beatra capabilities are acceptable.

Risk: User-approved speech and voice-clone tool calls can spend Beatra account credits.

Mitigation: Require explicit approval before paid clone or speech stages, read live pricing before submission, use unique client_request_id values, and verify final billing with task or ledger results.

Risk: Voice cloning can upload user-selected files and may involve likeness or voice rights.

Mitigation: Use only authorized voice samples, inspect files before upload, and treat file access as insufficient proof of consent.

Risk: The package stores a shared bearer credential in ~/.beatra.

Mitigation: Keep the credential private, preserve restrictive file permissions, avoid exposing tokens in chat, logs, command arguments, or environment variables, and use the bundled uninstall flow when disconnecting.

Risk: Automatic package updates are silent unless disabled.

Mitigation: Use the documented update controls to disable automatic updates or check available updates before replacement when managed-environment review is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/visitor-desk-voice)
- [Beatra skill homepage](https://beatra.ai/skills/visitor-desk-voice)
- [Visitor desk voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline shell commands and JSON payloads; generated audio artifacts are returned by Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 labeled voice clips from a supplied reception script; paid speech or clone calls require user approval and task polling.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
