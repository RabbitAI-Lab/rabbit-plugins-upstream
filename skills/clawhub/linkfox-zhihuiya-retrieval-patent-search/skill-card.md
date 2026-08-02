## Description: <br>
Searches the Zhihuiya (PatSnap) patent database with Analytics query expressions and returns matching patent identifiers, publication numbers, basic metadata, hit counts, and saved JSON results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and patent researchers use this skill to discover patents that match field-scoped Analytics expressions, then review returned publication numbers, titles, dates, assignees, and hit counts before requesting deeper patent details through companion skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent search expressions, session metadata, and result data are sent to LinkFox/Zhihuiya and full responses are persisted locally. <br>
Mitigation: Use only in workspaces with appropriate storage controls, avoid confidential patent strategy unless retention is acceptable, and clear saved response and cache files when no longer needed. <br>
Risk: Automatic feedback reporting may disclose user sentiment or task context to the Feedback API. <br>
Mitigation: Review feedback behavior before installation and avoid sharing sensitive user context in feedback content. <br>
Risk: Search calls consume credits, and larger result limits increase cost. <br>
Mitigation: Start with small limits, confirm the query expression with the user before expanding or paginating, and avoid automatic retries or keyword changes after empty or failed results. <br>
Risk: The skill returns list-level patent data only, not full bibliographic, legal-status, family, image, or full-text details. <br>
Mitigation: Use returned patent IDs or publication numbers with the appropriate companion skills when deeper patent details are needed. <br>


## Reference(s): <br>
- [智慧芽-检索式专利检索 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-retrieval-patent-search) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown summary with tabular patent results plus saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid LinkFox API key; writes full API responses under a local linkfox session data directory and uses a 24-hour cache for repeated parameter combinations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
