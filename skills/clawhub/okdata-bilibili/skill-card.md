## Description:

Public Bilibili data through okdata: videos, trending board, accounts, comment replies, backup. 9 endpoints, $0.002–$0.0025 a call. Use when a task needs Bilibili data. 通过 okdata 取B站公开数据：视频、热榜、账号、评论回复、backup。9 个接口，每次 $0.002–$0.0025。

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Bilibili videos, trending searches, account profiles and uploads, comments, and comment replies for research and analysis. It provides paged results through okdata and tells the user where the data came from.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to an external API. The security assessment was benign with medium confidence and partial scan coverage; it does not establish what data a live request may send.

Mitigation: Review the endpoint and parameters before each call, send only the identifiers or search terms needed, and keep the API key in the designated environment or client configuration without printing or placing it in a URL.

Risk: Each data call is paid, and requesting additional pages incurs additional charges.

Mitigation: Tell the user the expected call cost before the first paid request, set a max_price where applicable, and fetch more pages only when needed.

## Reference(s):

- [Bilibili API capabilities and contracts](https://okdata.online/apis/bilibili/?src=skill-okdata-bilibili)
- [okdata agent setup](https://okdata.online/agents.md)
- [ClawHub release page](https://clawhub.ai/conn-ho/skills/okdata-bilibili)
- [Publisher profile](https://clawhub.ai/user/conn-ho)

## Skill Output:

**Output Type(s):** [Text, API data, Guidance]

**Output Format:** [Text or Markdown containing fetched Bilibili data, source attribution, and, when useful, JSON request examples or shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are paged; each additional page requires another API call. Paid calls cost $0.002–$0.0025 each.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
