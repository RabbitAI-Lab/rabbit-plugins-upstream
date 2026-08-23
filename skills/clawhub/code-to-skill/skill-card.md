## Description:

Converts building-code PDFs, GB standards, industry rules, and regulations into queryable agent skills that index clauses by trigger, preserve mandatory-force wording, extract tables as JSON, and map cross-standard references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn supplied building-code or regulation PDFs into local, searchable agent skills with clause files, structured data tables, mandatory-force maps, and cross-reference documentation. It supports design-review and standards lookup workflows but does not replace professional legal, architectural, or engineering judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to run local Python extraction commands and create files in the user's workspace.

Mitigation: Run it only when the requested file operations are expected, keep paths scoped to the intended workspace, and review generated files before loading or publishing them.

Risk: Converting untrusted PDFs can produce incorrect, misleading, or unsafe generated skills.

Mitigation: Review and scan generated skills before deployment, especially when source documents are untrusted.

Risk: Optional parser dependencies can change the local environment if installed.

Mitigation: Install optional dependencies only after explicit confirmation and prefer existing trusted extraction tools when available.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/51comic/skills/code-to-skill)
- [README](artifact/README.md)
- [References](artifact/references/REFERENCES.md)
- [Changelog](artifact/CHANGELOG.md)
- [Calibre Downloads](https://calibre-ebook.com/download)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with local shell commands, generated Markdown files, and structured JSON table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local skill files from user-provided documents; optional parser dependency installation requires user confirmation.]

## Skill Version(s):

1.0.6 (source: evidence.release.version, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
