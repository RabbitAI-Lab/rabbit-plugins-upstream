## Description:

根据图片、主题与风格要求，生成自然贴合且可直接发布的中文朋友圈文案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wenmao030](https://clawhub.ai/user/wenmao030)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate concise, natural Chinese WeChat Moments captions that match a provided image or image description, theme, and style preference. It is intended for personal social captions rather than long-form social articles, hard-sell advertising, or professional marketing copy for other platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be selected automatically for closely related caption-writing requests because implicit invocation is enabled.

Mitigation: Review the selected skill and user intent before relying on output, especially when the request could target another platform or marketing format.

Risk: Image-based captions can introduce unsupported locations, dates, relationships, events, or emotions when visual details are ambiguous.

Mitigation: Use only visible or user-provided facts and ask for missing image, theme, or style details when they cannot be reliably inferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wenmao030/skills/generate-moments-copy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown numbered list or single Chinese caption text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces publish-ready Chinese copy directly; defaults to 10 distinct caption options when the user does not specify quantity, and returns one final caption when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
