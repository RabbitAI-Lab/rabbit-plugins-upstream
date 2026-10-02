## Description:

Review code on two axes: Standards for code quality and Spec for requirements alignment, with support for multi-agent parallel review, visual review, and file-based handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to review code changes against both implementation quality and stated requirements before merge. It supports task-level and branch-level reviews, impact analysis, annotations, and optional visual reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads repository diffs and may scan local project Python files.

Mitigation: Run it only in repositories where review agents are allowed to inspect source files and diffs.

Risk: The skill can write review artifacts such as record.md, review_annotations.json, JSON reports, and HTML reports.

Mitigation: Confirm the intended output paths before use and review generated files before committing them.

Risk: Generated HTML reports may be unsafe to open for untrusted repositories until escaping is fixed.

Mitigation: Avoid opening generated HTML reports from untrusted codebases; prefer terminal, Markdown, or JSON output when reviewing untrusted input.

Risk: Multi-agent review results can contain incorrect or misleading findings.

Mitigation: Treat findings as review guidance and verify important claims against the diff, tests, and project requirements before acting.

## Reference(s):

- [Confidence Scoring Guide](references/confidence-scoring.md)
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/code-review)
- [Publisher Profile](https://clawhub.ai/user/paudyyin)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown review reports, structured JSON reports, terminal text, annotations, and optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write review artifacts such as diff files, annotation stores, JSON reports, HTML reports, and record files in the workspace.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
