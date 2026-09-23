## Description:

SenseAudio Music Generation API for creating AI-generated lyrics and songs, with lyrics generation, song generation controls, and async task polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scikkk](https://clawhub.ai/user/scikkk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call SenseAudio APIs for generating lyrics, creating full songs, and polling asynchronous generation tasks. It is intended for workflows that need API request examples, response shapes, and configuration guidance for music generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Music prompts, lyrics, titles, style choices, and related generation metadata are sent to SenseAudio's external API.

Mitigation: Submit only content approved for that external service and avoid confidential or regulated text unless SenseAudio's data handling terms have been reviewed.

Risk: The SenseAudio API key can be exposed if copied into shared logs, examples, or source files.

Mitigation: Store SENSEAUDIO_API_KEY in an environment variable or secret manager and redact authorization headers from logs and shared snippets.

Risk: Asynchronous lyrics or music generation can remain pending, fail, or return outputs that are unsuitable for publication.

Mitigation: Poll task status, handle FAILED responses, and review generated lyrics and audio before downstream or commercial use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scikkk/skills/music-gen)
- [SenseAudio Lyrics Create Documentation](https://senseaudio.cn/docs/song/lyrics_create)
- [SenseAudio Lyrics Pending Documentation](https://senseaudio.cn/docs/song/lyrics_pending)
- [SenseAudio Music Create Documentation](https://senseaudio.cn/docs/song/music_create)
- [SenseAudio Music Pending Documentation](https://senseaudio.cn/docs/song/music_pending)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, bash, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENSEAUDIO_API_KEY and uses asynchronous task polling for lyrics and music generation.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
