## Description:

Bilibili Video Transcriber helps agents retrieve and validate Bilibili subtitles, fall back to official summaries or speech-to-text, and prepare structured video summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adolescen-he](https://clawhub.ai/user/adolescen-he)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Bilibili videos into reliable subtitles, summaries, and Feishu-ready documentation. It is most useful when platform subtitles need validation or when missing subtitles require a controlled fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and store Bilibili session cookies.

Mitigation: Avoid login flows unless they are required, run the skill in an appropriate workspace, and remove stored cookie files after use.

Risk: The skill can publish transcript or comment content to Feishu/Lark through locally authenticated tooling.

Mitigation: Confirm the target workspace and document before publishing, review generated content first, and avoid authenticated document creation when it is not needed.

Risk: Fallback transcription can download or process video/audio and may run long local speech-to-text jobs.

Mitigation: Get user consent before downloading media, check system load for long jobs, and prefer subtitle or official-summary paths when they are sufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adolescen-he/skills/bilibili-video-transcriber)
- [Feishu Wiki API reference](references/feishu-wiki-api.md)
- [Series discovery reference](references/series-discovery.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON transcript or summary artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local transcript, subtitle, comment, and summary files; may create or update Feishu/Lark documents when authenticated tooling is available.]

## Skill Version(s):

3.0.0 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
