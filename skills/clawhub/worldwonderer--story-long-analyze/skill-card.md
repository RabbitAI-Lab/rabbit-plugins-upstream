## Description:

Analyzes long-form web novels through a staged pipeline covering the opening chapters, character structure, plot beats, emotional pacing, setting, relationships, final analysis reports, and style profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story-development agents use this skill to deconstruct legally provided long-form fiction into reusable analysis artifacts for planning, critique, and writing guidance. It supports staged review from a three-chapter preview through full-book summaries, plot rhythm, emotional modules, character files, setting files, reports, and style profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves full novel text and derived analysis outputs locally.

Mitigation: Install only when local storage of the source text is acceptable, avoid sensitive book titles or entity names, and use a contained output directory.

Risk: Unsafe file-name or shell-command handling could write outside the intended folder or run unintended commands.

Mitigation: Use explicit paths, keep outputs in a contained directory, and review any generated shell command before execution.

Risk: Optional topic-decision backfill could update the wrong file if the target is ambiguous.

Mitigation: Approve backfill only for the intended topic-decision file and skip the step when the target cannot be confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Long Novel Deconstruction Notes](references/deconstruction-notes.md)
- [Novel Material Decomposition Methodology](references/material-decomposition.md)
- [Output Templates](references/output-templates.md)
- [Pipeline Operations Reference](references/pipeline-ops.md)
- [Style Profile Generator](references/style-profile-generator.md)
- [Style Profile Protocol](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown analysis files, structured tables, concise status prompts, and final reports written under the selected book analysis directory.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may pause after the opening-three-chapter preview before continuing to full-book analysis; outputs can include local copies of user-provided source text.]

## Skill Version(s):

1.1.20 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
