## Description: <br>
Story Long Analyze guides an agent through staged deconstruction of long-form Chinese web fiction, producing structured analysis of opening chapters, chapter summaries, plot arcs, characters, settings, pacing, emotional hooks, and style. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[9438190](https://clawhub.ai/user/9438190) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, and story-development agents use this skill to analyze legally provided long-fiction manuscripts and convert the results into reusable writing guidance, including plot structure, character profiles, emotional pacing, and style profiles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow copies or saves the source manuscript under `拆文库/{书名}/原文/`, which can retain user-provided copyrighted or sensitive text in the local workspace. <br>
Mitigation: Use only texts the user has the right to analyze and store, run the skill in a controlled workspace, and remove manuscript backups when they are no longer needed. <br>
Risk: Full analysis can create a sizable output folder and may take a long time because later stages process many chapters and generate multiple reports. <br>
Mitigation: Use the Stage 1 pause point to review the quick preview before continuing, and rely on `_progress.md` to resume or stop long runs cleanly. <br>
Risk: The workflow may conditionally update an existing project-root `选题决策.md` planning file after generating the deconstruction report. <br>
Mitigation: Review planning-file changes before accepting them and keep the project under version control or maintain a backup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/9438190/skills/story-long-analyze) <br>
- [Declared OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Long-form fiction deconstruction reference](references/deconstruction-notes.md) <br>
- [Novel material decomposition methodology](references/material-decomposition.md) <br>
- [Deconstruction output templates](references/output-templates.md) <br>
- [Pipeline operations reference](references/pipeline-ops.md) <br>
- [Style profile generation SOP](references/style-profile-generator.md) <br>
- [Style profile protocol](references/style-profile-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis files and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a structured local analysis workspace under `拆文库/{书名}/`, including manuscript backup, progress tracking, chapter analysis, plot and character files, summary reports, and style profiles.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
