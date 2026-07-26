## Description: <br>
Converts videos, subtitle files, or large course directories into structured illustrated notes, using read-only analysis unless the user explicitly confirms downloads, file writes, or course imports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pavelpeng7](https://clawhub.ai/user/pavelpeng7) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, knowledge workers, and learners use this skill to plan or execute video-to-article workflows, including subtitle-based study guides, Obsidian notes, and batch course imports. It is intended for workflows where the user can confirm access rights, output locations, and side-effect operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide downloads, generated shell scripts, and local file writes as part of its video-to-notes workflow. <br>
Mitigation: Use the default read-only preview posture until the user confirms the workflow, output directory, and any generated script before execution. <br>
Risk: Some video sources may require cookies or login state, which can expose sensitive account credentials if mishandled. <br>
Mitigation: Confirm the user has access rights, keep cookies out of chats, logs, notes, and repositories, and delete temporary credential files after use. <br>
Risk: Batch course import and screenshot planning can modify many local files and produce generated scripts. <br>
Mitigation: Review planned file paths and generated commands first, restrict outputs to the intended course or vault directory, and run CPU-heavy ffmpeg extraction sequentially. <br>
Risk: Git operations can publish generated notes or sensitive artifacts unintentionally. <br>
Mitigation: Require explicit confirmation for commits and separate confirmation for any git push. <br>
Risk: Transcripts, ASR output, and visual interpretation can contain errors or omit important visual context. <br>
Mitigation: Prefer existing subtitles when available, mark possible transcription errors or visual-only content, and review generated notes before relying on them. <br>


## Reference(s): <br>
- [Large Course Ingest: Six-Phase Details](references/large-course-ingest-workflow.md) <br>
- [Single Video Ingest: Classification and Output Strategy](references/single-video-ingest.md) <br>
- [Subagent Context Optimization](references/subagent-context-optimization.md) <br>
- [Subtitle Study Modes](references/subtitle-study-modes.md) <br>
- [ClawHub skill page](https://clawhub.ai/pavelpeng7/skills/video-to-article) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notes and study materials with inline shell commands, optional JSON screenshot plans, and local file outputs when confirmed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide generation of Obsidian notes, screenshots, preprocessed subtitle text, course indexes, and git commands after explicit user confirmation.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
