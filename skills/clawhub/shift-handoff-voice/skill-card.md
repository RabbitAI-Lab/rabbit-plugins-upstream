## Description:

Turns a written shift-handoff checklist into a labeled set of 8 to 20 spoken voice clips, one cue per clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Shift teams use this skill to turn their existing handoff checklist into short, consistently voiced audio cues for outgoing, incoming, and unfinished work. A staff voice clone is optional and requires voice rights and separate approval for paid work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device authorization grants access to Beatra tools beyond the voice-clip task.

Mitigation: Review the full scope of the Beatra approval before connecting, and revoke the device authorization when it is no longer needed.

Risk: A shared bearer token is stored locally under ~/.beatra.

Mitigation: Protect local account access and use the documented disconnect procedure when removing the final Beatra skill.

Risk: The bundled client can silently update package-owned files.

Mitigation: Turn off automatic updates with the documented client setting if changes require review before installation.

Risk: Voice cloning and speech generation can incur charges or use a staff member's likeness without adequate permission.

Mitigation: Confirm voice rights, review current prices, and approve clone and speech stages separately before submitting paid requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/shift-handoff-voice)
- [Beatra skill homepage](https://beatra.ai/skills/shift-handoff-voice)
- [Shift handoff voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio files]

**Output Format:** [Labeled checklist and MP3 voice clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 10 clips; requests outside 8 to 20 require cost confirmation.]

## Skill Version(s):

0.1.7 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
