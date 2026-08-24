## Description:

Translate a specific article from ai-thoughts/docs/ into Simplified Chinese, writing the output to an exactly-same-filename "-chn.md" file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content maintainers use this skill to create Simplified Chinese Markdown versions of explicitly selected articles while preserving filenames, links, code, commands, and technical terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes a translated Markdown file, and the artifact uses both ai-thoughts/docs and docs wording for paths.

Mitigation: Before approving execution, verify the reported source file, exact output path, and any overwrite decision.

Risk: Translation may accidentally alter code, commands, links, product names, or technical terms.

Mitigation: Review the generated Markdown against the source and confirm that preserved terms, code blocks, image references, and links remain unchanged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/translate-to-chn)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown translation file plus a concise text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-selected source article and confirmation before writing or overwriting output.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
