## Description:

管理社交空间相册，支持扫码登录、浏览、上传、下载照片及创建相册，并基于非官方 API 自动化操作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to manage QZone-style photo albums by logging in with a local cookie file, listing albums and photos, uploading or downloading photos, and creating albums.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cookie file can expose full QQ/QZone session access.

Mitigation: Keep cookies.json local, out of shared folders and version control, restrict file permissions, and delete it when finished.

Risk: The skill can modify a live account through unofficial album APIs.

Mitigation: Manually confirm any upload, download, album-creation, or album-selection command before running it.

Risk: Unofficial API behavior may change without notice.

Mitigation: Test with non-critical albums first and verify returned album IDs, photo IDs, and results after each operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/qq-zone-photo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell command examples and JSON cookie-file guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on local cookie files and may make live album changes when executed by an agent.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
