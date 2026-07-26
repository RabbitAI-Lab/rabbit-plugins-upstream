## Description: <br>
Zhipu web search lets an agent run configurable web searches through Zhipu AI's BigModel web search API using curl or the bundled shell wrapper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whyhit2005](https://clawhub.ai/user/whyhit2005) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add current web search capability to an agent, including engine selection, result-count control, recency filtering, and optional search-intent recognition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Zhipu/BigModel under the configured Zhipu account and may contain sensitive information if supplied by the agent or user. <br>
Mitigation: Avoid sending secrets, private internal details, or sensitive personal data in queries, and use a revocable API key where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/whyhit2005/skills/zhipu-web-search) <br>
- [Zhipu BigModel web search API endpoint](https://open.bigmodel.cn/api/paas/v4/web_search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and the ZHIPU_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
