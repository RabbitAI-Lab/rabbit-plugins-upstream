## Description:

图书智能解读系统 analyzes a book from a title, chapter text, notes, excerpts, or PDF content and produces a structured Chinese-language reading report in Markdown and HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mongoliatooop](https://clawhub.ai/user/mongoliatooop)

### License/Terms of Use:

MIT-0

## Use Case:

External readers, knowledge workers, and agents use this skill to turn a book title or supplied book material into a practical reading report with summaries, concepts, critique, action guidance, a mind map, and related-book recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain excerpts, notes, or other user-provided book material.

Mitigation: Review and sanitize Markdown and HTML reports before sharing them outside the intended audience.

Risk: Optional Mermaid CDN rendering in HTML can load a third-party script when the file is opened.

Mitigation: Keep the default self-contained HTML rendering unless the user explicitly accepts external script loading.

## Reference(s):

- [图书智能解读系统 output specification](artifact/references/report-spec.md)
- [ClawHub skill page](https://clawhub.ai/mongoliatooop/skills/book-analyst)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown report and single-file HTML report, with Mermaid mind map syntax when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces paired local files named <book>-解读报告.md and <book>-解读报告.html; HTML is intended to be self-contained unless optional Mermaid CDN rendering is enabled.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
