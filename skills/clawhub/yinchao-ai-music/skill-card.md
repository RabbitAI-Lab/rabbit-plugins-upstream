## Description:

使用音潮（YinChao）生成可播放的完整 AI 歌曲和 BGM；支持文字或歌词转歌曲、歌词谱曲演唱、参考音频风格创作、歌曲续写或延长，以及纯歌词创作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeydqyuan](https://clawhub.ai/user/joeydqyuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to generate complete AI songs, BGM, lyrics-only drafts, reference-audio-based songs, and song extensions through YinChao. It is intended for music creation workflows, not search, playback, transcription, conversion, mixing, or mastering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, lyrics, public audio URLs, and uploaded local audio may be sent to YinChao under the user's API key and may consume quota or paid usage.

Mitigation: Tell users before local audio upload, require `YINCHAO_API_KEY` from the environment, and direct users to check YinChao account quota or billing when usage fails.

Risk: Users may provide reference audio they are not authorized to use.

Mitigation: Proceed only with audio the user has rights to upload or reference; ask a brief clarification when the file source or rights are unclear.

Risk: Artist or song imitation requests can create copyright or likeness concerns.

Mitigation: Transform specific artist or song requests into higher-level musical traits and avoid promises to clone voices, melodies, lyrics, or distinctive recordings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/joeydqyuan/skills/yinchao-ai-music)
- [YinChao Open Platform](https://platform.yinchaoyongxian.com/?register_channel=clawhub)
- [Complete Song and Lyric Generation](references/generation.md)
- [Reference Audio Creation](references/reference.md)
- [Song Extension](references/extension.md)
- [Delivery and Error Handling](references/delivery.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown for user-facing results, with shell commands and compact JSON handled internally by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return song titles, listening or download links, complete lyrics, or a task ID for later polling.]

## Skill Version(s):

1.3.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
