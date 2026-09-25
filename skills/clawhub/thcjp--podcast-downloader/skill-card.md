## Description:

Downloads Xiaoyuzhou podcast audio and show notes, converts audio to MP3, and saves the results in a structured local folder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to download Xiaoyuzhou podcast episodes, convert audio to MP3 for offline playback, and save show notes as Markdown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad routing text may cause an agent to invoke command or file-write tools for unrelated coding, debugging, or deployment tasks.

Mitigation: Use the skill only for Xiaoyuzhou podcast downloads and ignore the broad coding/debugging/deployment routing claims.

Risk: Podcast download workflows run shell commands and write local files.

Mitigation: Review proposed commands before execution and set PODCAST_DIR to a directory the user controls.

Risk: The package references helper files that are not included, so documented commands may fail until setup is completed.

Mitigation: Confirm the required scripts and dependencies are present, including curl, jq, and ffmpeg, before relying on the workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/podcast-downloader)
- [Clawdis Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with bash command examples and generated local audio/Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PODCAST_DIR, AUDIO_QUALITY, and KEEP_M4A environment variables when commands are executed.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
