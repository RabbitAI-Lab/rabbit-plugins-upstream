## Description:

Creates WeChat public account articles as styled HTML for the WeChat rich-text editor, including article structure, image and video placeholders, and a closing call to action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qiyuany](https://clawhub.ai/user/qiyuany)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and editors use this skill to draft or convert articles into WeChat editor-ready HTML, with inline styling, media placeholders, and suggested titles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writing to a user-specified path could overwrite an existing file.

Mitigation: Confirm the output path and check for an existing file before writing.

Risk: Unreplaced image or video placeholders could appear in the published article.

Mitigation: Review the HTML and replace each media placeholder before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qiyuany/skills/wechat-article-formatter)
- [WeChat-compatible CSS components](artifact/references/css-components.md)
- [HTML article template](artifact/assets/template.html)

## Skill Output:

**Output Type(s):** [Code, Text]

**Output Format:** [HTML file with brief text notes and title suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media placeholders require manual replacement before publication.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
