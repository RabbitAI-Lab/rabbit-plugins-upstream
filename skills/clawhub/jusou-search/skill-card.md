## Description:

用聚搜GO（Jusou）给 Agent 联网搜索：一个 Key 调 8 个搜索引擎（Exa / Tavily / Serper / SerpApi / Brave / 博查 / 百度 / AnySearch），按积分计费、失败不扣分。用户要求联网搜索、查最新信息、找资料、核实事实、多引擎对比，或提到 Tavily/Exa/Serper 替代、聚合搜索时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[laomao-ai](https://clawhub.ai/user/laomao-ai)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和使用联网 Agent 的用户可通过一个 Jusou API Key 查询多个搜索引擎，获取最新信息、查找资料、核实事实或比较搜索结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The search script can send the API key to a configurable destination, and searches may expose private or confidential query content.

Mitigation: Verify that the configured service destination is trusted and uses HTTPS. Do not send private or confidential information in searches.

## Reference(s):

- [聚搜GO service and API key setup](https://jusouai.cn)
- [聚搜GO search API endpoint](https://jusouai.cn/v1/search)

## Skill Output:

**Output Type(s):** [Text, Links]

**Output Format:** [Plain text search results with titles, URLs, snippets, and a billing summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports engine selection, result count, search depth, time range, and optional multi-engine result merging.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
