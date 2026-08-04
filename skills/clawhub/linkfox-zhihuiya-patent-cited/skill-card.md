## Description: <br>
从智慧芽（PatSnap）查询专利被引用数据，包括被引用次数和引用专利详情。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to query Zhihuiya (PatSnap) forward citation counts and citing-patent details for one or more patent IDs or publication numbers. It supports citation comparison and factual patent influence analysis while avoiding patent valuation or investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent queries and full API responses are sent to LinkFox and stored locally, including cache files. <br>
Mitigation: Use the skill only when those data flows are acceptable, avoid submitting sensitive patent queries without approval, and review or remove saved response and cache files after use. <br>
Risk: The skill can direct the agent to install an auxiliary remote onboarding skill when authentication or credits fail. <br>
Mitigation: Require explicit user confirmation before installing auxiliary skills or downloading remote skill packages. <br>
Risk: Feedback text can be sent to a separate LinkFox feedback endpoint. <br>
Mitigation: Require explicit confirmation before submitting feedback and avoid including confidential user content in feedback payloads. <br>
Risk: The service consumes credits based on returned result count. <br>
Mitigation: Tell the user before additional or repeated lookups and avoid automatic retries or broad query expansion. <br>


## Reference(s): <br>
- [智慧芽-专利被引用 API 参考](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-cited) <br>
- [LinkFox Tool Gateway API](https://tool-gateway.linkfox.com/zhihuiya/patentCited) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables, JSON API responses, and saved JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key; caches repeated requests for 24 hours and saves full API responses locally.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
