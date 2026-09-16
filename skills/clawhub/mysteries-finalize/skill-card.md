## Description:

Updated Phase 4: Smart Thumbnail Generation to output a `Featured_v2` variant that scales the full image and fills margins seamlessly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and media operators use this skill to finalize Farsight video projects by preparing transcripts, localized subtitles, and thumbnail variants from completed video, audio, and base image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the workflow in the wrong project folder could rename, move, or organize files outside the intended Farsight final asset set.

Mitigation: Use an explicit invocation and verify the `Renders/Final/` directory plus required video, audio, and thumbnail assets before processing.

Risk: Subtitle localization may expose transcript text to the configured translation provider.

Mitigation: Confirm the translation provider and data handling expectations before translating sensitive or private transcript content.

Risk: Thumbnail resizing and cropping rules can alter visual framing or remove footer text in generated variants.

Mitigation: Review generated thumbnail outputs, especially `Featured` and `Featured_v2`, before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/mysteries-finalize)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown workflow guidance with inline shell commands and generated transcript, subtitle, thumbnail, and folder outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires project media assets, ffmpeg, whisper-cli with a local model, Python image processing, and subtitle translation dependencies.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
