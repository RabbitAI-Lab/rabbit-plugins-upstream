## Description:

z-card-image renders user-provided copy into PNG card images, including posters, paginated article cards, X-style long post images, and WeChat cover images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aatrooox](https://clawhub.ai/user/aatrooox)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and publishing agents use this skill to turn short copy, long-form text, social post data, and article titles into shareable PNG card images with template-specific layout rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-controlled content is rendered through local browser tooling.

Mitigation: Run the skill in a contained workspace, limit network access, and review content from untrusted sources before rendering.

Risk: Generated images may include fixed third-party branding.

Mitigation: Check outputs for unwanted branding such as 早早集市 or made by Jinx, and set explicit footer or asset options when supported.

Risk: Article rendering can be risky when fed raw HTML or remote-resource Markdown.

Mitigation: Use plain text inputs where possible and avoid remote-resource Markdown in article rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aatrooox/skills/z-card-image)
- [poster-3-4 template specification](references/poster-3-4.md)
- [article-3-4 template specification](references/article-3-4.md)
- [x-like-posts template specification](references/x-like-posts.md)
- [tweet-thread compatibility note](references/tweet-thread.md)
- [wechat-cover-split template specification](references/wechat-cover-split.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [PNG image files with concise Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and Google Chrome; output paths should be explicit and kept within the workspace.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
