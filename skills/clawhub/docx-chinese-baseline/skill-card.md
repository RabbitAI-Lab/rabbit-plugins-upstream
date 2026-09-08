## Description:

Provides a locked design-token baseline for Chinese Word/DOCX documents and WeChat-native article layouts, including fixed title, section, body, and heading-color rules plus conversion recovery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, document automation users, and agents use this skill when producing Chinese DOCX or WeChat-native articles that must preserve consistent typography, heading color, CJK rendering, and editable text through conversion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated DOCX formatting may differ from the intended baseline after html-to-docx conversion or fallback generation.

Mitigation: Reopen the generated DOCX and verify title, section, and body sizes; heading color; CJK font rendering; editability; and the reported conversion path.

Risk: Recovery paths may use an existing html-to-docx pipeline or a python-docx rebuild, which can still produce layout differences.

Mitigation: Review generated documents for formatting correctness and keep the same locked tokens when retrying or rebuilding programmatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/docx-chinese-baseline)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, code, text]

**Output Format:** [Markdown report with conversion path, verification checklist results, and output file path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide use of an existing html-to-docx pipeline or a python-docx fallback while preserving the same visual tokens.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
