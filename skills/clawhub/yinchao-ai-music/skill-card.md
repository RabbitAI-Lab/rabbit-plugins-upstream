## Description:

音潮 AI 音乐创作 helps agents generate playable complete songs, instrumental music, BGM, lyrics-to-song outputs, reference-audio creations, and song continuations with YinChao.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeydqyuan](https://clawhub.ai/user/joeydqyuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill through an agent to generate complete songs, instrumental tracks, BGM, lyrics-only drafts, reference-audio creations, or song continuations with YinChao. It is intended for music creation workflows, not music search, playback, transcription, audio conversion, mixing, or mastering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends prompts, lyrics, and user-selected audio to YinChao's service.

Mitigation: Use it only when the user intends to use YinChao, avoid submitting sensitive content, and notify the user before uploading local audio.

Risk: The skill requires a YinChao API key, and misplaced credentials could be exposed.

Mitigation: Provide the key through environment variables or configured key files, keep credential files out of version control, and do not paste full keys into chat.

Risk: Reference audio or style requests could imply unauthorized copying of protected music or artist identity.

Mitigation: Use only audio the user has rights to provide and translate artist or song requests into broad musical attributes rather than cloning voices, lyrics, melodies, or recordings.

## Reference(s):

- [YinChao Open Platform](https://platform.yinchaoyongxian.com/?register_channel=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/joeydqyuan/skills/yinchao-ai-music)
- [Generation Guide](references/generation.md)
- [Reference Audio Guide](references/reference.md)
- [Extension Guide](references/extension.md)
- [Delivery and Error Handling Guide](references/delivery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with song titles, audio links, lyrics, task IDs when needed, and concise setup or error guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated lyrics, playable or downloadable audio URLs, and status information for long-running tasks.]

## Skill Version(s):

1.5.0 (source: server evidence, release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
