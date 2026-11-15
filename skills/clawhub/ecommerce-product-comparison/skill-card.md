## Description:

当用户需要对比已选商品、比较规格和卖点差异，或准备竞品对照表时使用。输入 2–5 个商品链接或商品资料，输出注明价格口径、信息缺口和来源的商品差异表。在线商品能力支持抖音与小红书，其他平台可基于用户提供的资料分析。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要比较电商商品的用户，基于用户选定的 2–5 个商品链接、平台 ID 或资料整理规格、价格条件、卖点和信息缺口。结果保留来源并标注可比性，证据不足时不强行给出排名。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a mutable @latest CLI package could expose available credentials if the package is compromised.

Mitigation: Review and trust the CLI package and publisher before execution; avoid using an unpinned latest release when credentials are available.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown 商品对比表，附来源、价格口径、信息缺口和简要分析]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [比较用户指定商品；在线支持抖音和小红书，其他平台依据用户提供的资料分析。]

## Skill Version(s):

0.1.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
