## Description:

Use when someone wants an original AI song with vocals — sung lyrics, a style prompt track, or source audio for a music video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to guide an agent through generating original vocal songs from lyrics and style prompts with the MiniMax music-2.5 model on Replicate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install multiple unpinned remote skills with automatic confirmation before use.

Mitigation: Review the referenced PrunaAI skills before installation, prefer pinned or reviewed versions, and avoid installing the full suite unless it is needed.

Risk: Lyrics, style prompts, and generated-song requests are sent to Replicate and MiniMax.

Mitigation: Do not submit secrets, private lyrics, regulated data, or content that cannot be shared with those external services.

## Reference(s):

- [music-2.5 on ClawHub](https://clawhub.ai/pruna-ai/skills/music-2-5)
- [MiniMax music-2.5 Replicate prediction endpoint](https://api.replicate.com/v1/models/minimax/music-2.5/predictions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REPLICATE_API_TOKEN; ffmpeg and ffprobe are needed only for slicing and assembly in the music-video workflow.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
