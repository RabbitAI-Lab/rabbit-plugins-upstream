## Description:

当用户需要提炼商品主图卖点、主副标题或安排商品图片信息层次时使用。提供商品链接或商品资料，输出主图标题、副标题、卖点短句与配图建议；可按需参考同类商品。在线商品能力支持抖音与小红书，已有资料可直接写作。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营者和商品内容创作者，用商品资料或支持的平台商品信息起草主图标题、副标题、卖点短句和配图建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 在线查询会将商品链接、标识符和搜索词发送给 SocialDataX，并可能消耗付费积分。

Mitigation: 无需在线补充时直接提供商品资料进行写作；在线使用前确认查询内容，并考虑使用经过审查且固定版本的 CLI。

Risk: 在线调用需要 SocialDataX API 凭据。

Mitigation: 仅在运行环境中提供必要凭据，并避免将 API Key 放入生成文件。

## Reference(s):

- [SocialDataX Documentation](https://socialdatax.com/docs)
- [ClawHub release](https://clawhub.ai/devinchen2014/skills/ecommerce-main-image-copywriter)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [中文 Markdown，含主副标题、卖点短句、配图建议及事实依据或待补信息]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [通常提供三套文案；每套聚焦一个有依据的核心价值，并包含最多三条卖点短句。]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
