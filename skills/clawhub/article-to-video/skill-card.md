## Description:

Converts Word, PDF, text, and Markdown articles into narrated videos with generated visuals, TTS voiceover, subtitles, background music, and scene transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unique-memory](https://clawhub.ai/user/unique-memory)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, educators, marketers, and developers use this skill to turn long-form documents into narrated MP4 videos with matching visuals, subtitles, thumbnails, and optional background music.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text can be sent to cloud TTS services by default and, in AI image mode, summarized into prompts for an external image tool.

Mitigation: Avoid sensitive or proprietary documents unless approved, and use the offline TTS fallback or template-slide mode when external processing is not acceptable.

Risk: Generated audio, image, video, cache, and progress files may persist locally after runs.

Mitigation: Review output directories and periodically clear generated cache and temporary media files according to local data handling requirements.

Risk: The background-music remove command permanently deletes local BGM files.

Mitigation: Back up reusable media assets and confirm the target style and filename before running the remove operation.

Risk: Dependencies should be kept on patched versions.

Mitigation: Review dependency minimums before deployment and update package pins or constraints to meet current security policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/unique-memory/skills/article-to-video)
- [Project homepage](https://github.com/unique-memory/article-to-video)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with bash commands; generated artifacts include JSON scene and image manifests, MP3 audio, PNG slides, MP4 video, SRT subtitles, and JPEG thumbnails.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local scripts for parsing, slide creation, TTS generation, video assembly, subtitle burning, background music management, caching, and resume progress.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
