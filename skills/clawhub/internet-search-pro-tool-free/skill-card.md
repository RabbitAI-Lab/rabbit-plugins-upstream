## Description: <br>
联网搜索助手 helps an agent run single-query web searches, filter results, and return concise structured summaries with source links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users can ask an agent to search for current information such as news, weather, real-time data, product details, or recent topic updates. The skill is intended for single-query lookup and summary, not batch search, export, history, or multi-turn research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags this release for review because the requested agent authority is broader than a simple web search helper usually needs. <br>
Mitigation: Use it only when web search is needed, review its behavior before deployment, and narrow or remove local read, glob, grep, and shell execution permissions unless they are specifically required. <br>
Risk: Search queries, external search services, or callback behavior could expose sensitive prompts, secrets, or private personal data. <br>
Mitigation: Use non-sensitive queries, do not enter secrets or private personal data, and require clear documentation of external query and callback behavior before broader use. <br>
Risk: Some artifact text describes unsupported create, export, or broad SEO behavior that may confuse the intended search-only scope. <br>
Mitigation: Treat the supported scope as single-query personal information retrieval and verify any broader behavior with the publisher before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/internet-search-pro-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-style structured search summaries with source links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns about 3-5 results for a single query; free edition does not support multi-turn search, batch queries, result export, or search history.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
