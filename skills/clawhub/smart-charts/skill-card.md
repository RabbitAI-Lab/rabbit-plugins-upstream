## Description:

Intelligent chart generation and data analysis skill. Reads user-supplied data files (CSV/Excel/JSON), analyzes data characteristics with LLM assistance, auto-recommends and generates interactive ECharts visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect tabular CSV, Excel, TSV, TXT, or JSON files, choose an appropriate chart type, and generate interactive ECharts HTML visualizations with data-backed written interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transform code is screened but executed in-process rather than inside an OS-level sandbox.

Mitigation: Use trusted transform snippets and run the skill with runtime containment appropriate for the dataset sensitivity.

Risk: Generated self-contained HTML chart files may include the underlying data used for rendering.

Mitigation: Avoid highly sensitive datasets unless the output directory and downstream sharing path are controlled.

Risk: The skill reads user-selected local data files and writes chart artifacts to disk.

Mitigation: Install and run it only when local file access and generated HTML output are acceptable for the environment.

## Reference(s):

- [Smart Charts Reference](artifact/references/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)
- [ClawHub Publisher Profile](https://clawhub.ai/user/neuhanli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands; generated artifacts are self-contained HTML files with JSON status and preview output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local chart files, data previews, plot statistics, and optional annotations; no network access is required by the skill.]

## Skill Version(s):

8.1.1 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
