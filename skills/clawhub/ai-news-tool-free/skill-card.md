## Description: <br>
每日新闻获取工具,通过 API 获取每日新闻摘要与详情,兼容按日期查询、热点排行、分类筛选与详情阅读。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch daily news lists, inspect ranked hot news, filter by category, and read individual article details through an agent-assisted workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to use shell commands and network requests to fetch news. <br>
Mitigation: Install only if that execution model is acceptable, and review commands before running them in sensitive environments. <br>
Risk: The skill includes file-saving, caching, and unrelated analytics or report-generation guidance. <br>
Mitigation: Treat local file writes and caching as opt-in actions, and avoid analytics or report-generation use until the publisher narrows those instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-news-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fetched news summaries, article details, command examples, local cache guidance, and API response handling notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
