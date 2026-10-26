## Description:

Unwrap hard-wrapped Markdown prose into one line per paragraph, while keeping code fences, tables, headings, setext headings, lists, blockquotes, hard line breaks, and YAML frontmatter intact. Use when a Markdown file was written with hard line breaks at a fixed width and needs to become one paragraph per line, when checking a folder of Markdown files for hard-wrapped prose (for CI), or when the user asks to unwrap, reflow, or un-hard-wrap Markdown. Handles CJK text without adding spaces between Chinese or Japanese characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to normalize hard-wrapped Markdown into one line per paragraph or check repositories for hard-wrapped prose while preserving documented Markdown structures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing reformatted files can overwrite existing content, and unusual Markdown layouts may not be preserved as intended.

Mitigation: Preview changes, confirm the selected files, use version control or a copy, and review the output, especially for unusual layouts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/unwrap-markdown)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [Markdown files with prose paragraphs unwrapped]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves documented Markdown structures and hard line breaks; supports CJK text and CRLF line endings.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
