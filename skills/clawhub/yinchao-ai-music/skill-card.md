## Description:

YinChao AI Music helps an agent create complete playable AI songs and BGM from prompts or lyrics, generate lyrics, adapt reference audio, and extend existing songs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[joeydqyuan](https://clawhub.ai/user/joeydqyuan)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to generate songs, BGM, lyrics, reference-audio music variations, and song extensions through the YinChao platform. It is intended for music creation workflows, not music search, playback, transcription, conversion, mixing, or mastering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated songs and user-selected reference or extension audio may be sent to the YinChao platform.

Mitigation: Tell users before uploading local audio, use only audio they have rights to use, and rely on the platform only for the requested creation task.

Risk: API keys could be exposed if users paste credentials into chat.

Mitigation: Configure the YinChao API key through environment variables or local config files, and do not ask users to share full keys in conversation.

Risk: Requests to imitate specific artists or songs could lead to voice cloning or protected musical replication.

Mitigation: Translate those requests into high-level style, era, instrumentation, tempo, mood, and vocal-characteristics guidance without promising voice cloning or copying protected melodies, lyrics, or recordings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/joeydqyuan/skills/yinchao-ai-music)
- [YinChao open platform](https://platform.yinchaoyongxian.com/?register_channel=clawhub)
- [Complete song and lyric generation](references/generation.md)
- [Reference audio creation](references/reference.md)
- [Song extension](references/extension.md)
- [Delivery and error handling](references/delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with song titles, audio links, lyrics, concise status guidance, and configuration instructions when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID for later status checks when generation is submitted without waiting.]

## Skill Version(s):

1.4.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
