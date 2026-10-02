## Description:

Data Analyzer helps agents analyze, summarize, and compare Excel, CSV, Word, PDF, TXT, and Markdown files, including folder scans, data aggregation, statistics, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and other users can use this skill to have an agent inspect local folders or selected files, extract tabular and document text, summarize findings, compare files, and prepare reports. It is most relevant when the user explicitly asks for local file or folder analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recursively reads supported local files and may surface sensitive extracted text or table contents in its outputs.

Mitigation: Use it only on explicit folders or files that are appropriate for analysis, and review generated summaries or reports before sharing them.

Risk: The Python dependencies are not pinned, which can produce different behavior across environments or over time.

Mitigation: Install the dependencies in a trusted virtual environment and pin versions before operational use.

Risk: Some advertised chart, report, merge, or multi-format output capabilities may be broader than the included implementation.

Mitigation: Confirm that required report or visualization features are implemented in the installed release before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tobewin/skills/data-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, generated reports, Python code snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce analysis summaries, extracted document text, tabular statistics, charts, and report files when the agent implements or runs the provided Python workflow.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
