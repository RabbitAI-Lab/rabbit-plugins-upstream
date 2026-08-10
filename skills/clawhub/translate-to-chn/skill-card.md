## Description:

Translates an explicitly selected article from ai-thoughts/docs into Simplified Chinese and writes a matching -chn.md Markdown file after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, writers, and maintainers use this skill to create Simplified Chinese Markdown translations for one explicitly chosen article while preserving filenames, links, code blocks, and technical terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or overwrite translated Markdown files.

Mitigation: Require explicit confirmation of the source path, output path, and overwrite decision before writing.

Risk: Translation may alter technical terms, commands, code, links, or article structure.

Mitigation: Preserve code blocks, inline code, commands, URLs, image references, Markdown structure, and named technical terms verbatim.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/translate-to-chn)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown file plus concise status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or overwrites a -chn.md translation file only after explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
