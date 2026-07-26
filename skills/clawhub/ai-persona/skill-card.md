## Description: <br>
一个支持多AI人格召唤与协作的MCP协议服务器，可用于代码分析、产品设计等多场景智能协作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to list or summon AI personas and route analysis, product design, or other collaboration tasks to the selected persona service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users for an API key and stores XBY_APIKEY in a plaintext .env file in the working directory. <br>
Mitigation: Use a dedicated, low-privilege API key and install only in workspaces where .env will not be committed, shared, or reused for unrelated secrets. <br>
Risk: The skill contacts xiaobenyang.com and mcp.xiaobenyang.com to fulfill persona requests. <br>
Mitigation: Review the external service and avoid sending sensitive prompts, proprietary code, or regulated data unless the service is approved for that use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/ai-persona) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY; API responses are returned as raw JSON and summarized for the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
