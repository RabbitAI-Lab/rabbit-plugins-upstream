## Description:

Turn a written elder-checkup schedule into one elder checkup voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and office staff use this skill to turn an existing elder-checkup schedule into a labeled set of spoken notice clips. It plans each cue from the supplied schedule, can use a catalog or authorized cloned voice, and submits paid Beatra speech tasks for the final audio pack.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra account authority through a shared local credential.

Mitigation: Install only when that account access is acceptable, keep the Device Token private, and use the bundled uninstall flow to disconnect when the package is no longer needed.

Risk: Executable package files can update silently by default.

Mitigation: Disable automatic updates when reviewed code must remain fixed, and review the package again before re-enabling updates.

Risk: Schedules, names, and voice samples may be health-adjacent or personally sensitive.

Mitigation: Provide only material the office is authorized to send to Beatra, require voice rights before cloning, and keep the skill's no-diagnosis boundary intact.

## Reference(s):

- [Elder Checkup Voice Pack on ClawHub](https://clawhub.ai/beatra-ai/skills/elder-checkup-voice)
- [Elder Checkup Voice Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to generated MP3 audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 one-cue voice clips; paid tasks return task IDs, audio MIME type, duration, size, and net charged credits.]

## Skill Version(s):

0.1.2 (source: server evidence release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
