## Description:

使用 EasyPost 自动填充或发布哔哩哔哩（B站）视频或动态。Use when 用户需要向 B站 投稿视频或发布图文动态。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gybin02](https://clawhub.ai/user/gybin02)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Bilibili creators use this skill to prepare or publish video submissions and image-text dynamics through EasyPost, using an already logged-in Chrome session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An already logged-in browser session could publish content to the wrong account or submit unintended files or text.

Mitigation: Use a trusted EasyPost installation and verify the logged-in account, selected files, and final content before publishing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/gybin02/skills/bilibili-upload)
- [Bilibili Creator Center](https://member.bilibili.com)
- [Bilibili Dynamics](https://t.bilibili.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown instructions with a Bash example containing a JSON payload]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The example configures video or image-text content, metadata, and media asset paths for EasyPost.]

## Skill Version(s):

1.0.0 (source: frontmatter; server release 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
