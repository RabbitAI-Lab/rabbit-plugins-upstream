## Description:

Reads local TXT, Markdown, DOCX, PDF, and HTML files and produces source-grounded summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All rights reserved (skill documentation; MIT applies only to .py code)

## Use Case:

People reviewing local documents use this skill to get a brief summary, a section-by-section summary with source locations, or answers focused on a specific question.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Summarizing local files may expose sensitive document contents.

Mitigation: Provide explicit file paths and avoid sensitive documents unless needed.

Risk: The skill permits file writing despite being intended for summarization.

Mitigation: Require a clear user request before writing any file.

Risk: Package license metadata conflicts with the document-level license scope.

Mitigation: Review the included license and attribution text before reusing or redistributing the skill.

## Reference(s):

- [Summarize File on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/summarize-file)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summary or question-focused answer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to three sentences; optional section summaries cite source locations.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
