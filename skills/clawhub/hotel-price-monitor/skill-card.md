## Description:

酒店降价监控与多平台比价助手，同时搜索多个旅游平台实时价格帮你比价省钱，支持按酒店名称精确比价、按城市搜索酒店列表、创建降价监控任务，多旅游平台数据直连。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and booking assistants use this skill to search hotel options by city and date, compare a named hotel across travel platforms, and prepare structured price-watch requests for follow-up by the host agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel names, cities, stay dates, and occupancy details are sent to the publisher's proxy service for live price lookup.

Mitigation: Review the proxy operator, network requirements, and retention policy before installation, and avoid sending unnecessary personal or booking details.

Risk: The bundled script contains an embedded shared proxy token.

Mitigation: Remove and rotate the embedded token and provide deployment-specific credentials through a managed secret or environment variable.

Risk: Result ordering is commission-aware when prices tie, which can affect platform recommendations.

Mitigation: Disclose commission-based tie-breaking and verify that user-facing recommendations still present all comparable platform prices clearly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-price-monitor)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Conversational Markdown with JSON outputs from the bundled Python comparison script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script emits hotel search and comparison JSON; price-watch requests are structured for the host agent to schedule and notify.]

## Skill Version(s):

1.1.6 (source: server release evidence; artifact frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
