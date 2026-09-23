## Description:

Locked design-token baseline for Chinese Word/DOCX documents and WeChat-native article layouts, specifying 23/18/16 px typography, deep-blue headings, layout restrictions, conversion recovery, and verification checks for consistent editable output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content producers, and agents use this skill to typeset Chinese DOCX files or WeChat-native articles with a locked visual baseline, especially when html-to-docx conversion loses styles or fails on Windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unintentional baseline changes can make Chinese DOCX and WeChat article output inconsistent across documents.

Mitigation: Treat the 23/18/16 px sizes, #1a3a5c heading color, and WeChat layout constraints as locked tokens; change the skill intentionally before changing generated documents.

Risk: DOCX conversion may lose styles or fail on Windows.

Mitigation: Reopen and verify the DOCX for expected sizes, heading color, CJK rendering, and editability; use the documented recovery or programmatic rebuild path when conversion fails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/docx-chinese-baseline)

## Skill Output:

**Output Type(s):** [Guidance, Configuration]

**Output Format:** [Markdown/text guidance with conversion and verification checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; output may include the chosen target style, conversion path, verification results, and output file path.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
