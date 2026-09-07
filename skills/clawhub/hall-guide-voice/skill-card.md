## Description:

Turn a written hall window list into one hall guide voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External service-hall operators and their agents use this skill to turn an existing window list into a labeled voice clip pack. It plans 8 to 20 cues, handles catalog or authorized cloned voices, and submits one text-to-speech task per slot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared Beatra device token with broad media and wallet capabilities.

Mitigation: Review the requested account scope before installation, keep the credential in the documented private file only, and use the bundled uninstall workflow when disconnecting the device.

Risk: The bundled client silently self-updates executable package files by default.

Mitigation: Use the documented update controls to disable automatic checks when locked-down updates are required, and rely on the package's manifest and checksum verification for accepted updates.

Risk: Paid clone and speech requests can spend Beatra credits or duplicate work if retried incorrectly.

Mitigation: Require a visible cost card before each paid stage, use one opaque client request ID per logical request, and retry only with byte-identical arguments after transport uncertainty.

Risk: Voice cloning can misuse a staff likeness if file access is treated as consent.

Mitigation: Proceed with cloning only after an authorized sample and documented likeness rights are confirmed.

## Reference(s):

- [Hall guide voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hall-guide-voice)
- [Beatra skill homepage](https://beatra.ai/skills/hall-guide-voice)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, audio files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated MP3 audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled slot list before paid clone or speech requests; successful speech tasks return audio MIME type, duration, size, and net charged credits.]

## Skill Version(s):

0.1.2 (source: server release metadata and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
