## Description: <br>
Searches the Zhihuiya (PatSnap) patent database with Analytics query expressions and returns matching patent IDs, publication numbers, basic patent fields, and hit counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to discover patents matching a Zhihuiya Analytics expression, inspect result counts, and decide whether to page through or send returned patent IDs to companion detail skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent-search queries and the LinkFox API key are sent to a LinkFox-controlled endpoint. <br>
Mitigation: Install and run only when the LinkFox endpoint is trusted, keep the API key scoped appropriately, and do not override LINKFOX_TOOL_GATEWAY to an untrusted host. <br>
Risk: Full API responses may be retained in generated linkfox data and cache directories. <br>
Mitigation: Review and clean the generated linkfox session and cache files according to local data-retention requirements, especially when patent results contain sensitive search context. <br>
Risk: Each search can consume paid credits, and repeated pagination or query changes can increase cost. <br>
Mitigation: Start with a small limit, avoid automatic retries or query rewrites, and ask the user before paging or expanding result volume. <br>


## Reference(s): <br>
- [智慧芽-检索式专利检索 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-retrieval-patent-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance] <br>
**Output Format:** [Markdown result summaries with saved JSON API responses and optional inline JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved under a linkfox session data directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
