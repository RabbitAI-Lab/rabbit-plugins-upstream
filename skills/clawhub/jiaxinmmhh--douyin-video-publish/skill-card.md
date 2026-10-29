## Description:

帮助创作者在抖音创作者中心发布成品视频、设置定时或批量排期，并核对发布队列。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT

## Use Case:

抖音创作者和运营人员可在视频与文案准备完成后，用此技能完成上传、填写标题与简介、设置合集和排期，并核对发布状态。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup can delete unintended videos, and the setup instructions call for disabling browser sandbox protection.

Mitigation: Preserve sandbox protection and use a dedicated browser profile. Keep deletion in dry-run mode until the exact video identity and scheduled status are verified; do not delete published content.

Risk: A publishing dry run still uploads the video and saves a screenshot; retrying failed batch items without checking may repeat an action.

Mitigation: Use private output paths, make screenshots optional, and verify the account state before retrying failed items.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/jiaxinmmhh/skills/douyin-video-publish)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Shell commands with operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prepared video and copy; publishing actions can upload content.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
