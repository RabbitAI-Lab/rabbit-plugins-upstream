## Description:

智慧情境 DJ，自動偵測心情、天氣和時段，生成適合當下情境的播放列表並可控制 macOS Music.app 播放。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill on macOS to generate context-aware music playlists for work, exercise, sleep, commute, cafe, party, romantic, rainy, and morning listening modes. It can return playlist recommendations, JSON output, TTS-friendly text, configuration prompts, and Music.app playback actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control macOS Music.app playback by default.

Mitigation: Review commands before use and run with --no-play when you only want playlist recommendations.

Risk: The skill reads Music.app library metadata and caches playlist data under the user home directory.

Mitigation: Use only on trusted machines and review cached files under ~/.smart-playlist-dj if local music metadata is sensitive.

Risk: City-based weather lookups are sent to wttr.in.

Mitigation: Use --skip-weather where available or avoid setting sensitive location values.

Risk: AppleScript query handling is unsafe for arbitrary search text.

Mitigation: Avoid passing arbitrary search text until safe AppleScript escaping or another safe query mechanism is added.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/smart-playlist-dj)
- [wttr.in weather service](https://wttr.in/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text, with optional JSON playlist output and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May control macOS Music.app playback, cache playlist data under the user home directory, and use city-based weather lookups when weather detection is enabled.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
