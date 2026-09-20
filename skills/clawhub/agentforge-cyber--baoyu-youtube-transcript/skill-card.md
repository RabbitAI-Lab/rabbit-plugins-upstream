## Description:

Downloads YouTube video transcripts/subtitles and cover images by URL or video ID, with support for multiple languages, translation, chapters, speaker identification, and cached re-formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to extract YouTube captions, subtitles, metadata, thumbnails, and formatted transcript files from a YouTube URL or video ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read browser session cookies when YOUTUBE_TRANSCRIPT_COOKIES_FROM_BROWSER is set.

Mitigation: Leave that environment variable unset unless authenticated YouTube access is intentionally required, and run only from an approved browser profile.

Risk: The skill may dynamically acquire external runtimes or fallback tools when direct transcript retrieval is blocked.

Mitigation: Review the planned runtime and fallback tool commands before execution and run the skill in a controlled environment.

Risk: Transcript text, video metadata, descriptions, and thumbnails may be saved locally in the configured output directory.

Mitigation: Choose the output directory deliberately, apply normal data-handling controls, and remove cached files when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentforge-cyber/skills/baoyu-youtube-transcript)
- [Project Homepage](https://github.com/JimLiu/baoyu-skills#baoyu-youtube-transcript)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration]

**Output Format:** [Markdown transcript files, SRT subtitle files, JSON cache files, local image files, stdout status text, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can cache video metadata, raw transcript snippets, sentence segmentation, and cover images in a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
