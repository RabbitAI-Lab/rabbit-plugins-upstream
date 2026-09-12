## Description:

Archives WeChat Official Account articles and image-note pages from mp.weixin.qq.com into a local Markdown file with copied image assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[harven-droid](https://clawhub.ai/user/harven-droid)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to save WeChat articles or image notes into a chosen local folder as Markdown plus local assets for offline reference and review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image downloads may cause the local machine to fetch internal or very large non-image content.

Mitigation: Use --skip-images for lower-risk archives, or deploy only after restricting image downloads to approved HTTPS WeChat/CDN hosts with redirect checks and response-size limits.

Risk: The skill runs local Python and Node code, installs npm and pip dependencies, fetches WeChat pages, and writes Markdown plus assets to a user-selected folder.

Mitigation: Install and run it only in an environment where these local execution, network, dependency, and filesystem effects are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/harven-droid/skills/wechat-article-archive)
- [Publisher profile](https://clawhub.ai/user/harven-droid)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown files with local asset links, local image files, and JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Markdown path, assets directory, image counts, and image download failures; supports skipping image downloads.]

## Skill Version(s):

1.1.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
