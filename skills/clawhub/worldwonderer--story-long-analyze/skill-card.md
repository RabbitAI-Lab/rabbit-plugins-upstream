## Description:

Analyzes long-form web novels through a staged pipeline covering opening chapters, chapter summaries, plot structure, characters, setting, pacing, reader appeal, and writing style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, and story-development teams use this skill to deconstruct a legally available long-form fiction manuscript into reusable analysis of structure, character systems, setting, pacing, emotional beats, and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists a full source-text backup and extracted original-text excerpts in the workspace.

Mitigation: Use it only with source text you have rights to analyze, and run it in a workspace where storing the manuscript under 拆文库/{书名}/原文/ is acceptable.

Risk: The optional topic-decision backfill can edit 选题决策.md outside the main analysis output folder.

Mitigation: Review or disable that backfill path before execution when edits outside 拆文库/{书名}/ are not desired.

Risk: Long-running analysis may create many persistent Markdown outputs and progress files.

Mitigation: Review the generated output tree and _progress.md after execution, especially before sharing or committing the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [deconstruction-notes.md](references/deconstruction-notes.md)
- [material-decomposition.md](references/material-decomposition.md)
- [output-templates.md](references/output-templates.md)
- [pipeline-ops.md](references/pipeline-ops.md)
- [style-profile-generator.md](references/style-profile-generator.md)
- [style-profile-protocol.md](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, files, guidance]

**Output Format:** [Markdown files organized under a story analysis directory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent project files, including source-text backup, progress tracking, chapter analysis, plot and character notes, reports, and style guidance.]

## Skill Version(s):

1.1.16 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
