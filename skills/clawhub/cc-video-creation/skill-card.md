## Description:

CC Video Creation helps create FactSage videos through a story, animation, and upload workflow using local Manim or Ken Burns rendering, with optional Kling AI web UI steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and FactSage maintainers use this skill to turn prepared FactSage scripts into vertical short-form videos with voiceover, Manim or Ken Burns animation, and manual upload guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video rendering runs Python and ffmpeg in the FactSage project workspace.

Mitigation: Install and run the skill only in trusted FactSage workspaces, and review the scripts before execution.

Risk: Voiceover text may be sent to Edge TTS during audio generation.

Mitigation: Do not use private or sensitive scripts for voiceover unless that cloud text-to-speech exposure is acceptable.

Risk: Project media and segment directories are treated as trusted rendering input.

Mitigation: Use trusted media and segment files, and review generated videos before upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/cc-video-creation)
- [Publisher profile](https://clawhub.ai/user/northcap-group)
- [Kling AI web UI](https://klingai.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown instructions with inline shell commands and generated MP4 video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are written under projects/factsage/output/; voiceover uses Edge TTS when the rendering scripts are run.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
