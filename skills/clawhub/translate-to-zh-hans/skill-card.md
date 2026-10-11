## Description:

Translates a user-selected article from ai-thoughts/docs into Simplified Chinese and writes a matching -zh-hans.md file after approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and developers use this skill to create a Simplified Chinese Markdown version of one explicitly chosen article while preserving its technical content and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An existing translation could be overwritten.

Mitigation: Review the source and exact output path, check for an existing translation, and require explicit approval before writing or overwriting.

Risk: A translation could alter technical content or distort the source meaning.

Mitigation: Review the translated article against the source, preserving code, names, links, images, and Markdown structure.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/j3ffyang/skills/translate-to-zh-hans)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Simplified Chinese Markdown article and output path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a -zh-hans.md file only for a selected article after user approval; preserves code, links, and Markdown structure.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
