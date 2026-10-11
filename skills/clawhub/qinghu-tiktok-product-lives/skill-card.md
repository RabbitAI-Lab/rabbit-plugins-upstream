## Description:

按商品 ID 查询该商品关联的 TikTok 带货直播列表，帮助用户查看直播销售记录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

TikTok Shop 商家及运营人员可按商品 ID 查看相关带货直播，并整理直播记录以辅助商品分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node and qhkit on the local machine.

Mitigation: Preinstall a reviewed qhkit version and approve any local runtime changes before execution.

Risk: API tokens could be exposed or persisted during setup.

Mitigation: Supply the token through a secure secret mechanism rather than pasting or saving it during a run.

Risk: Product-live queries consume paid Qinghu credits, potentially more for larger results.

Mitigation: Check the current credit estimate and obtain user consent before paid or bulk queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-product-lives)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise summary with live-stream records; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a product ID; paid queries report the Qinghu credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
