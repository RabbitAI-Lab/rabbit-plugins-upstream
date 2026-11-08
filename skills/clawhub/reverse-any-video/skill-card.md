## Description:

Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage. Measure and watch it, rebuild every layer, then check the render against the original frame by frame. Use to reverse, recreate, replicate or copy a video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to reconstruct videos they have rights to use as editable HyperFrames projects, then compare the render with the source frame by frame.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud generation can consume paid credits without advance cost disclosure.

Mitigation: Set a credit ceiling and require a cost estimate before generation.

Risk: Video, faces, and voice recordings may be sent to cloud services by default.

Mitigation: Confirm which footage and recordings may be sent externally before generation; local rendering alone does not disable uploads.

Risk: The external CLI and provider data-retention behavior were unavailable for inspection, and the skill sends usage telemetry unless opted out.

Mitigation: Use a reviewed, fixed CLI version, opt out of telemetry if unwanted, and review provider data handling before sending sensitive media.

## Reference(s):

- [Matching what is drawn](references/match.md)
- [Re-shooting a person](references/people.md)
- [Animated and painted films](references/animated.md)
- [Opening a Reverse](references/start.md)
- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/reverse-any-video)

## Skill Output:

**Output Type(s):** [Files, Configuration, Shell commands, Guidance]

**Output Format:** [Editable HyperFrames project files with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reconstructed video layers and assets remain editable in the project.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
