## Description:

查询最多十位 TikTok 达人的详情，支持按用户 ID 或 @用户名查找。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts look up TikTok creator profiles by user ID or @username to assess audience and commerce metrics, including small batches of up to ten creators.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can install an unpinned package globally or change host tooling.

Mitigation: Provision and pin a trusted qhkit version in a managed environment before use.

Risk: API credentials and TikTok creator identifiers are handled by an external paid service.

Mitigation: Use platform-managed secret injection and share only identifiers approved for the lookup.

Risk: Paid lookups may incur variable charges, including after failed calls.

Mitigation: Check the estimate and obtain user consent before calling; review actual credits after each call.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-creator-detail)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports platform, period and sample size when applicable; discloses credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
