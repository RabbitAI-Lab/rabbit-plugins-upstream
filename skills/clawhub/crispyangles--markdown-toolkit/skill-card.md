## Description:

Swiss army knife for Markdown: TOC generation, MD-to-HTML conversion, formatting cleanup, HTML stripping, file merging, YAML frontmatter validation, and orphan link finding, with code-block-aware snippets and no support for LaTeX, DOCX, or rich document layout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crispyangles](https://clawhub.ai/user/crispyangles)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to produce and repair Markdown documents, generate tables of contents, convert Markdown to simple HTML, validate YAML frontmatter, merge Markdown files, and find reference-link issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HTML conversion and tag-stripping snippets may be mistaken for sanitizers for hostile or untrusted Markdown and HTML.

Mitigation: Use the snippets only for trusted documents; prefer pandoc or a maintained sanitizer when processing untrusted input.

Risk: The HTML examples load a stylesheet from a remote CDN, which can affect privacy, availability, and offline behavior.

Mitigation: Use a local stylesheet or remove the CDN reference when privacy-sensitive or offline operation matters.

Risk: Cleanup commands such as in-place whitespace edits can overwrite document content.

Mitigation: Run in-place commands only on files that are backed up or can be restored from version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crispyangles/skills/markdown-toolkit)
- [Simple.css stylesheet used by HTML examples](https://cdn.simplecss.org/simple.min.css)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with inline shell and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some snippets modify files in place or emit HTML; HTML conversion and stripping examples are not sanitizers for untrusted documents.]

## Skill Version(s):

3.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
