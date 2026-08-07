## Description:

歌詞隨唱伴侶 helps users practice songs with synchronized LRCLIB lyrics, slowed karaoke playback, repeated sections, lyric-writing aids, and Chinese, English, and Japanese translation views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to find lyrics, run terminal karaoke practice sessions, generate lyric-writing templates and rhyme guides, and compare song translations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lyrics or user-provided text may be sent to external lyric search and translation services.

Mitigation: Use the skill only with text suitable for third-party services, and avoid networked search or translation when content is private or sensitive.

Risk: The URL-based lyrics retrieval command can fetch arbitrary URLs.

Mitigation: Use trusted LRCLIB IDs or public URLs only; do not supply private, internal, or sensitive URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/karaoke-companion)
- [LRCLIB API](https://lrclib.net/api)
- [LibreTranslate endpoint](https://libretranslate.com/translate)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown and terminal text with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local lyric cache, song text files, or translation comparison files when the user runs the provided scripts.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
