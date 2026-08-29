## Description:

Turn a written shift handoff checklist into one shift handoff voice clip per labeled cue. This shift handover voice studio records each handover checklist audio and shift change voice from the list the desk already wrote, then delivers 8 to 20 shift handoff clip files. Use it for shift handoff voice packs that keep one cue on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams, shift leads, and desk staff use this skill to turn an existing written shift handoff checklist into labeled voice clips for outgoing, incoming, unfinished, and follow-up cues. Agents use it to plan the clip list, confirm consent and billing before paid voice work, submit Beatra speech or clone tasks, and report returned audio task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authority for speech generation, voice cloning, wallet spending, task access, artifact access, uploads, and cancellation.

Mitigation: Install only for agents that should use those Beatra account capabilities, and reconnect with the documented authorization flow only after the user explicitly accepts that scope.

Risk: The skill stores a persistent Beatra Device Token on disk.

Mitigation: Keep the token only in the documented private credentials file, avoid exposing it in chat, logs, command arguments, or environment variables, and revoke or uninstall the connection when no longer needed.

Risk: The skill sends non-billable installation registration data including package, version, platform, and installation reference.

Mitigation: Treat installation registration as telemetry and install only where that registration is acceptable.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use the documented update controls to disable automatic updates when review-before-update is required.

Risk: Voice cloning and speech generation can consume Beatra credits and may create duplicate charges if paid requests are replayed incorrectly.

Mitigation: Show a separate billing confirmation before each paid stage, use one opaque client request identity per logical request, and retry uncertain submissions only with byte-identical arguments.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/shift-handoff-voice)
- [Beatra skill homepage](https://beatra.ai/skills/shift-handoff-voice)
- [Shift handoff voice workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline JSON and shell command examples, plus generated audio clip files returned by Beatra tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 20 labeled shift handoff clips; defaults to MP3 speech output unless the user-approved task parameters differ.]

## Skill Version(s):

0.1.1 (source: release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
