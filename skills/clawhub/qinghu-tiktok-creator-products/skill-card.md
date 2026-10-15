## Description:

按 TikTok 达人 user_id 查询其通过直播、视频或橱窗带货的商品。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

TikTok 商家、营销人员和分析师用它查询指定达人带货商品，了解直播、视频及橱窗的商品构成。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install unpinned remote software globally or change the host environment persistently.

Mitigation: Review installation steps; prefer a preinstalled, pinned qhkit version and approve global installs or shell profile changes explicitly.

Risk: API tokens may be exposed or persisted on the host during configuration.

Mitigation: Prefer an environment variable for the token and avoid sharing or storing it in shell history.

Risk: Product lookups are paid, and larger result sets may cost more than the base estimate.

Mitigation: Check the current estimate, obtain user consent before paid calls, and report the actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-creator-products)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report the queried scope and actual credits charged; product details may require a separate lookup.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
