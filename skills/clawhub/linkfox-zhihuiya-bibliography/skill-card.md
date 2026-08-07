## Description: <br>
通过专利 ID 或公开号查询智慧芽专利数据库中的著录信息，包括标题、申请人、发明人、分类号、摘要、引用和优先权等元数据。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve factual patent bibliography records when they already have a patent ID or publication number. It is suited for inventor, applicant, assignee, classification, abstract, citation, priority, and expiration-date lookup workflows, not open-ended patent search or legal analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent lookup requests and API responses are sent to LinkFox services, and full patent responses are stored locally. <br>
Mitigation: Use the skill only when users accept LinkFox processing and local response storage; handle saved JSON files according to the sensitivity of the patent data. <br>
Risk: The artifact instructs agents to send broad feedback and user-intent content to a separate LinkFox feedback API. <br>
Mitigation: Remove or disable automatic feedback behavior unless the user explicitly approves sending feedback content to LinkFox. <br>
Risk: The LINKFOX_TOOL_GATEWAY environment variable can direct requests to a non-default host. <br>
Mitigation: Set LINKFOX_TOOL_GATEWAY only to a trusted endpoint, or leave it unset to use the default LinkFox gateway. <br>
Risk: Bibliography queries consume credits dynamically, especially for batch requests. <br>
Mitigation: Tell users about expected credit use before large or repeated queries and avoid automatic retries or query expansion after failures or empty results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-bibliography) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [Zhihuiya bibliography API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Saved JSON files with stdout JSON or summaries, plus Markdown tables or organized sections for user-facing answers.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts patentId or patentNumber JSON parameters, stores full responses under a local linkfox session directory, and uses a 24-hour cache for repeated parameter combinations.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
