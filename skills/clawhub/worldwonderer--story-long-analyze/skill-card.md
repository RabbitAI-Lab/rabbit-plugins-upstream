## Description:

Analyzes long-form web novels through a staged decomposition pipeline covering opening chapters, chapter summaries, character structures, pacing, emotional hooks, settings, relationships, reports, and style profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, editors, and agent users can use this skill to analyze legally held long-form fiction and produce structured writing-reference materials. It is intended for literary criticism, editorial review, and writing-planning workflows rather than source-text redistribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves a full local copy of the novel and derived analysis, including substantial style examples.

Mitigation: Use it only with text the user has rights to process, avoid sensitive manuscripts unless local storage is acceptable, and review or remove stored source text and excerpts before sharing outputs.

Risk: The skill can modify an optional planning file outside the main analysis folder.

Mitigation: Review or disable the optional topic-decision backfill before running it in projects where planning files should remain unchanged.

Risk: The security verdict is suspicious because of local persistence and file-modification behavior.

Mitigation: Review the skill behavior before deployment and scan generated outputs before importing them into downstream writing workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Long-Form Story Deconstruction Notes](references/deconstruction-notes.md)
- [Novel Material Decomposition Methodology](references/material-decomposition.md)
- [Output Templates](references/output-templates.md)
- [Pipeline Operations Reference](references/pipeline-ops.md)
- [Style Profile Generator SOP](references/style-profile-generator.md)
- [Style Profile Protocol](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown files, structured analysis text, progress notes, and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes analysis artifacts under a local book-specific directory and may ask the user whether to continue after the opening-chapter preview.]

## Skill Version(s):

1.1.18 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
