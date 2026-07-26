## Description: <br>
Video to Notes helps an agent turn local or online videos into structured study notes by extracting audio, transcribing speech with Whisper, and organizing the transcript into reviewable notes, outlines, diagrams, and quick-reference material. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yll-kb](https://clawhub.ai/user/yll-kb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, professionals, and developers use this skill to convert course videos, lectures, tutorials, meetings, talks, and documentaries into searchable transcripts and structured learning notes. It is useful when a user provides a local media path or supported video URL and wants concise, reviewable Markdown notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may download a video or read a local media file and create transcript or note files that contain sensitive or copyrighted content. <br>
Mitigation: Use explicit source media and output locations, follow applicable platform and content-use rules, and review or remove generated files when they are no longer needed. <br>
Risk: The workflow may require media and transcription tools such as ffmpeg, ffprobe, openai-whisper, and optional URL-download dependencies. <br>
Mitigation: Review any dependency installation prompt and the exact command before approving installation or execution. <br>
Risk: Generated transcripts and notes can omit, mishear, or over-summarize source material. <br>
Mitigation: Check important claims against the transcript or original video before using the notes for decisions, publication, or study-critical review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yll-kb/skills/video-to-notes) <br>
- [Workflow reference](references/workflow.md) <br>
- [Note templates](references/note-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown notes and timestamped transcript text, with optional Mermaid diagrams, tables, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local media files or supported URLs, normally up to three files per request; writes transcript text and note files to an explicit or default output location.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
