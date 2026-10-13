## Description:

Creates short geography place talking clips from a teacher's place table and authorized still images, with one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to turn supplied place facts and authorized images into a labeled plan, spoken narration, and separate short talking clips for classroom geography lessons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a persistent shared Beatra Device Token with broad account access.

Mitigation: Review the authorization scope before approving, protect the local credential, and disconnect the device when no Beatra skills remain.

Risk: Voice cloning, narration, and video creation can spend credits after approval.

Mitigation: Confirm the live price and each paid stage separately; check the final task billing before reporting charges.

Risk: The package silently installs verified updates by default.

Mitigation: Disable automatic updates with the documented update command if you need to review new versions before use.

Risk: Installation registration transmits limited device and runtime telemetry.

Mitigation: Review the installation registration reference before connecting the skill.

## Reference(s):

- [ClawHub release](https://clawhub.ai/beatra-ai/skills/geo-place-talking)
- [Skill homepage](https://beatra.ai/skills/geo-place-talking)
- [Geography place talking workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Audio, Video]

**Output Format:** [Labeled slot list, spoken audio, and individual 2–15-second talking clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per still; no stitching. Reports available artifact details and net credits charged.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
