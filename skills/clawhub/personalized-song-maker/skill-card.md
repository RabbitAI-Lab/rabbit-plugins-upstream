## Description:

Turn a person's story and occasion into original lyrics and a newly generated song.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn a real story, occasion, and must-include details into approved lyrics and one generated personalized song, such as a birthday, wedding, anniversary, proposal, tribute, or team anthem.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra device token with broad media, task, artifact, and spending permissions.

Mitigation: Install only when those permissions are acceptable, keep the credential file private, revoke access from the Beatra Console when needed, and avoid sharing sensitive personal details beyond what the song requires.

Risk: The bundled client silently checks for and installs package-owned updates by default.

Mitigation: Turn automatic updates off before use when explicit change control is required; use the documented update check command to inspect available updates without replacing files.

Risk: Song generation is a paid asynchronous request, and duplicate submissions could create unintended charges.

Mitigation: Freeze the approved title, lyrics, prompt, and request ID before submission; recover and poll the original task before retrying or starting changed paid work.

Risk: Personalized songs can involve private names, memories, uploads, or sensitive story details.

Mitigation: Collect only details needed for the song, preserve private details marked for omission, and use upload behavior only when the user intentionally wants a specific local file sent to Beatra.

## Reference(s):

- [Story-to-song workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Personalized Song Maker homepage](https://beatra.ai/skills/personalized-song-maker)
- [Personalized Song Maker on ClawHub](https://clawhub.ai/beatra-ai/skills/personalized-song-maker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with approved lyrics, production direction, approval checkpoints, inline shell commands, task status, billing details, and returned audio artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One approved lyric draft and one paid song generation per run; terminal task and billing details are reported from Beatra responses.]

## Skill Version(s):

0.1.1 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
