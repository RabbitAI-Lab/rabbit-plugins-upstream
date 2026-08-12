## Description:

Karaoke Companion helps users practice singing with synchronized lyrics, karaoke playback, lyric-writing aids, and Chinese, English, and Japanese translation comparisons using LRCLIB lyrics with speed control and section repeat support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to search and prepare synced lyrics, practice karaoke-style playback, generate lyric-writing templates and rhyme prompts, and display multilingual lyric comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lyric searches and translation text may be sent to LRCLIB, DuckDuckGo, and LibreTranslate.

Mitigation: Avoid entering sensitive or personal text and install only if those third-party service calls are acceptable.

Risk: Optional Music.app sync can read currently playing track metadata.

Mitigation: Use Music.app sync only when sharing current track name, artist, and duration with the local skill flow is acceptable.

Risk: Untrusted lyric files or suspicious track metadata may contain terminal control characters.

Mitigation: Avoid opening untrusted lyric files or suspicious track metadata in the terminal until control-character sanitization is added.

Risk: Lyrics, translations, and generated song material may be cached locally under ~/.karaoke-companion.

Mitigation: Do not process sensitive lyrics or drafts unless local caching is acceptable; inspect or clear the cache directory as needed.

## Reference(s):

- [LRCLIB](https://lrclib.net)
- [LibreTranslate](https://libretranslate.com)
- [Karaoke Companion on ClawHub](https://clawhub.ai/xuan905/skills/karaoke-companion)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and terminal text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local cache files under ~/.karaoke-companion and may call LRCLIB, DuckDuckGo, LibreTranslate, and optional macOS Music.app sync.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
