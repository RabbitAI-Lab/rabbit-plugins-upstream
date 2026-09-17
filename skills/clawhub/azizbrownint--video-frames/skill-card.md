## Description:

Extract frames or short clips from videos using ffmpeg.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content reviewers use this skill to extract a video frame at the beginning, at a timestamp, or by frame index for inspection and sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The frame extraction script can overwrite the file passed with --out.

Mitigation: Choose the output path deliberately and avoid pointing --out at files that should be preserved.

Risk: The skill depends on ffmpeg being installed and available on PATH.

Mitigation: Install ffmpeg through a trusted package manager such as the declared Homebrew formula before use.

## Reference(s):

- [FFmpeg](https://ffmpeg.org)
- [video-frames on ClawHub](https://clawhub.ai/azizbrownint/skills/video-frames)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ffmpeg; writes the requested output image file and can overwrite an existing output path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
