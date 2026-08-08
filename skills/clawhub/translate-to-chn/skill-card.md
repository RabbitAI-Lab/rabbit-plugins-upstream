## Description:

Translates a user-selected Markdown article from ai-thoughts/docs/ into Simplified Chinese and writes an approved -chn.md copy while preserving code, links, images, and specified technical terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill when they need an explicitly selected ai-thoughts Markdown article translated into Simplified Chinese without changing the source file or auxiliary repository metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes translated Markdown files locally and could target an unintended path if the selected article or output path is wrong.

Mitigation: Confirm the source file and exact -chn.md output path with the user before writing.

Risk: An existing -chn.md translation could be overwritten.

Mitigation: Stop when an output file already exists and ask the user whether to overwrite, diff, or skip.

Risk: Translation could accidentally alter code, commands, file names, links, images, or product names.

Mitigation: Preserve code blocks, inline code, technical terms, image references, links, and named products verbatim while translating only surrounding prose.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown file with a translated Simplified Chinese article]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a same-name -chn.md copy only after the user approves the source path, output path, and overwrite behavior.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
