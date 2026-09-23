## Description:

三剪客 · 音乐生成 helps agents call a7w music-generation APIs for song creation, lyric generation, reference audio, voice cloning, audio export, and stem-related workflows using the user's own api.a7w.cn API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users can use this skill to configure an a7w API key, inspect the music_generation interface schema, and run music creation, lyric, audio export, and voice-style workflows from an agent-controlled CLI. It is intended for users who already have rights to any prompts, lyrics, public audio URLs, or voice samples they provide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads a user-provided a7w API key and sends it with API requests.

Mitigation: Use a dedicated key, keep it out of source control, revoke and recreate it if exposed, and use the default api.a7w.cn host unless testing in a controlled environment.

Risk: The bundled client can call broader a7w marketplace APIs and may spend account points beyond the advertised music workflow.

Mitigation: Review the command, app code, API name, and request body before execution, monitor point usage, and avoid repeated submissions of the same paid task.

Risk: Voice cloning and public audio URL inputs can involve sensitive recordings or third-party rights.

Mitigation: Provide only audio that the user is authorized to process, obtain clear consent for voice samples, and avoid voice cloning when rights or consent are unclear.

Risk: Generated songs, lyrics, stems, and exports may require separate content review before publication or commercial use.

Mitigation: Review generated content for policy, copyright, publicity, and platform requirements before distributing or using it commercially.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/2253128/skills/sanjianke-music-generation-kit)
- [a7w compute marketplace](https://api.a7w.cn/)
- [Getting started](references/getting-started.md)
- [Create music task API](references/api-create.md)
- [Query music task API](references/api-query.md)
- [Generate lyrics API](references/api-lyrics.md)
- [Mash up lyrics API](references/api-mashup_lyrics.md)
- [Optimize music style API](references/api-style.md)
- [Upload reference audio API](references/api-upload_audio.md)
- [Voice clone API](references/api-voice_clone.md)
- [Singer persona API](references/api-persona.md)
- [Vocal processing API](references/api-vox.md)
- [Lyric timing API](references/api-timing.md)
- [Export MIDI API](references/api-midi.md)
- [Export MP4 API](references/api-mp4.md)
- [Export WAV API](references/api-wav.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, configuration steps, and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some API calls are asynchronous and may require polling until task completion.]

## Skill Version(s):

1.0.5 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
