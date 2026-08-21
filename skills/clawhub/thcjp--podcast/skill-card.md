## Description:

播客 helps creators plan podcast episodes, draft scripts, prepare audio and video production guidance, generate social media clip ideas, and create distribution assets with Chinese-language interaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, podcast teams, and automation users use this skill to plan shows, write episode scripts, prepare production notes, suggest audio or video processing steps, and generate social media clip and growth materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local audio or video files, write output files, or propose media-processing commands.

Mitigation: Keep source media in the project workspace and review command paths and output targets before allowing file writes or command execution.

Risk: Podcast workflows can involve copyrighted audio, video, music, or transcript material.

Mitigation: Use original or properly licensed media and avoid processing copyrighted content without the necessary rights.

Risk: Some workflows may depend on API keys or credentials for external services.

Mitigation: Scope credentials to the project, store them in environment variables, and avoid committing keys or sensitive media metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/podcast)
- [ffmpeg download](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose episode structures, scripts, show notes, timestamps, ffmpeg or whisper commands, and media-processing parameters; actual media rendering requires external tools.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
