## Description:

story-long-analyze guides agents through a staged long-form web novel analysis pipeline covering opening chapters, character and setting structure, pacing, emotional hooks, summary reports, and style profile outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and fiction-development teams use this skill to analyze legally held long-form web novels and generate structured critique artifacts for story planning, pacing review, character and setting analysis, and style study.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists full source manuscripts and derived analysis files locally.

Mitigation: Use it only with text the user has rights to analyze, avoid sensitive manuscripts unless local persistence is acceptable, and delete or relocate the 拆文库 output when it should no longer remain on disk.

Risk: Resume and rerun behavior can overwrite or update generated analysis outputs.

Mitigation: Keep backups of manually edited analysis files before resuming a failed run or rerunning later stages.

Risk: The style-profile workflow can retain verbatim source excerpts as reusable anchors.

Mitigation: Review generated style-profile files before reuse and avoid sharing outputs that contain copyrighted or private source excerpts.

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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files, structured text reports, and inline shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local analysis workspace under 拆文库/{book}/, including source backups, progress state, chapter files, character and setting notes, summary reports, and style guidance.]

## Skill Version(s):

1.1.15 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
