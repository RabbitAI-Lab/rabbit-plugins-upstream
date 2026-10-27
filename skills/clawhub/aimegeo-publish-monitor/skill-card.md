## Description:

用户要求在 aimeGeo 同步账号、准备或执行发布、核验回执、检测 AI 引用或同题复测时使用。按实际能力和本次发布授权行动，不承诺收录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

面向使用 aimeGeo 的用户与代理，用于核对账号与平台能力、准备或执行已授权的内容发布，并检查真实回执、AI 引用和搜索收录状态。技能引导如实区分草稿、审核中、已公开和检测失败等结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Content could be submitted from the wrong account or without the user's authorization for that publication.

Mitigation: Confirm the destination account and content, and verify authorization for the current publication before submitting; keep the task in preparation when either check is incomplete.

Risk: Questions sent to selected AI services may be received by those services, and saved records or delayed monitoring settings may need review.

Mitigation: Use non-sensitive test questions and review saved records and delayed monitoring settings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xxjrq/skills/aimegeo-publish-monitor)
- [aimeGeo account connection](https://geo.aimmme.com/docs/accounts/)
- [aimeGeo publishing workflow](https://geo.aimmme.com/docs/publish-flow/)
- [aimeGeo AI citation checks](https://geo.aimmme.com/docs/ai-citations/)
- [aimeGeo GEO workflow](https://geo.aimmme.com/docs/geo-workbench/)
- [aimeGeo troubleshooting](https://geo.aimmme.com/docs/common-issues/)
- [aimeGeo platform directory](https://geo.aimmme.com/platforms/)
- [aimeGeo agent and skill help](https://geo.aimmme.com/docs/agent-skills/)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown instructions and concise operational status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report account and platform checks, publication status and links, or monitoring questions, channels, timestamps, and observed citations. Excludes credentials and private customer data.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
