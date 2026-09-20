## Description:

Helps an agent inspect and remove local AI watermark or provenance signals from user-owned or user-generated image and video files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through identifying, stripping, or cleaning AI watermark and provenance marks in media they own or generated/edited. It is intended for local CLI-assisted media processing with safeguards against paid-asset watermark removal and deceptive provenance claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may install or replace local media-processing software.

Mitigation: Use an isolated environment, pin or verify the package version, and avoid --force or --upgrade unless the user explicitly approves replacement.

Risk: The skill can strip provenance data from media files.

Mitigation: Process only media the user owns or generated/edited, keep originals, and stop when the user seeks to make deceptive origin claims.

Risk: Removal commands may overwrite files or produce partial results.

Mitigation: Use -o or output directories, confirm the output exists before reporting it, and report exact exit codes and caveats.

Risk: GPU, ffmpeg, and optional pixel dependencies can change which commands are available.

Mitigation: Run the bundled probe before choosing commands and avoid unavailable CUDA, video, or pixel-processing routes.

## Reference(s):

- [Remove AI Watermarks ClawHub listing](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Publisher profile](https://clawhub.ai/user/wiltodelta)
- [Project homepage](https://raiw.cc)
- [Project repository](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command recipes](references/commands.md)
- [Install extras](references/install.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON probe interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of cleaned media files through the CLI when the user authorizes a removal and an output path is supplied.]

## Skill Version(s):

1.0.9 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
