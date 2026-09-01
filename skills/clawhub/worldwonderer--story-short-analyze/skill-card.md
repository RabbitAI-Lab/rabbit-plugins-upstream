## Description:

Story Short Analyze helps agents deconstruct short-form Chinese web fiction into story structure, emotional beats, reversals, character functions, writing techniques, and reusable analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story-development agents use this skill to analyze legally held short fiction and produce reusable critique artifacts for downstream short-story writing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow backs up source text and generated reports in a local story-specific directory.

Mitigation: Use the skill only with works the user has rights to process, and review stored source backups before sharing or publishing the workspace.

Risk: Broad trigger phrases can invoke the full analysis pipeline when the user intended only casual discussion.

Mitigation: Confirm the user wants a complete short-story analysis before running the pipeline on provided text.

## Reference(s):

- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Output Contract](references/output-contract.md)
- [Output Templates](references/output-templates.md)
- [Material Decomposition](references/material-decomposition.md)
- [Source Story Quality](references/source-story-quality.md)
- [Analysis Report Style](references/analysis-report-style.md)
- [Short Genre Analysis](references/analysis-short-genres.md)
- [Short Hook Analysis](references/analysis-short-hooks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, JSON, Guidance]

**Output Format:** [Markdown reports, JSON metadata, and structured file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a source backup, analysis report, plot-node notes, writing-technique notes, and _meta.json under a story-specific output directory.]

## Skill Version(s):

1.1.17 (source: server release metadata; source skill frontmatter reports 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
