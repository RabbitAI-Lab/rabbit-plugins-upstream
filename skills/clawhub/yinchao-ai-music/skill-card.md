## Description:

音潮 AI 音乐创作 helps agents create complete AI songs and BGM with YinChao, including text-to-music, lyrics-to-song, reference-audio creation, song extension, and lyrics-only writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeydqyuan](https://clawhub.ai/user/joeydqyuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate original songs, BGM, lyrics, reference-audio-inspired songs, and song continuations through YinChao. It is intended for music creation workflows, not music search, playback, transcription, format conversion, mixing, or mastering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, lyrics, task IDs, and user-selected reference audio are sent to YinChao's platform.

Mitigation: Inform users before local audio upload, configure the API key through environment or documented dotenv paths, and only provide audio files the user has rights to use.

Risk: Requests to imitate a specific artist or song could lead to attempts to clone voices or reproduce protected material.

Mitigation: Convert those requests into higher-level musical traits such as genre, era, arrangement, tempo, mood, and vocal texture; do not promise voice cloning or replication of protected melodies, lyrics, or recordings.

## Reference(s):

- [音潮开放平台](https://platform.yinchaoyongxian.com/?register_channel=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/joeydqyuan/skills/yinchao-ai-music)
- [完整歌曲与歌词创作](references/generation.md)
- [参考音频创作](references/reference.md)
- [歌曲续写与延长](references/extension.md)
- [长任务、结果交付与错误处理](references/delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance]

**Output Format:** [Markdown summaries with song titles, audio links, lyrics, and optional task status details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long-running song generation can return a task ID for later status checks; reference and extension modes can use user-selected MP3/WAV audio up to 10 MB.]

## Skill Version(s):

1.4.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
