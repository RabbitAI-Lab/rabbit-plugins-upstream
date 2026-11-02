## Description:

投前 AI 图真实性质检。待检图 → 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。当用户说「投前检测」「图片质检」「检查有没有崩」「上架前把关」「这图能不能用」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and creative teams use the skill to assess AI-generated product images before listing, identify visual and platform-compliance issues, and get prompt corrections or rerun guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional automatic rerun helper may send confidential images to a cloud provider other than the one selected.

Mitigation: Use direct review calls or configure PROVIDER consistently for the entire process, and verify the destination with a dry run before uploading images.

Risk: Automatic reruns can incur additional cost, and image-read failures may be missed if only the checker exit status is considered.

Mitigation: Limit paid reruns, preserve prior reports, retain human review, and treat image-read errors as failures even when the checker exits successfully.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/detect-task)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown quality-review report with risk level, eight itemized checks, a release recommendation, and optional English prompt corrections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily Chinese report text; optional automatic rerun workflow.]

## Skill Version(s):

1.0.26 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
