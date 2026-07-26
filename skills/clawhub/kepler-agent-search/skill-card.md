## Description: <br>
Searches Bing, Zhihu, and Xiaohongshu through Kepler MCP tools so agents can find web results and extract content for research, comparison, and summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mylike2018](https://clawhub.ai/user/mylike2018) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to route web search and page-reading tasks across Bing, Zhihu, and Xiaohongshu, then return structured search results, article reads, or multi-source research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries, URLs, API keys, and research targets are sent to the third-party Kepler MCP provider and downstream search services. <br>
Mitigation: Use only when the user trusts the apisec.cn provider; avoid confidential prompts, internal URLs, proprietary research targets, and sensitive credentials. <br>
Risk: External search and content extraction can return incomplete, stale, or misleading web content. <br>
Mitigation: Have the agent cite sources, compare multiple engines for important tasks, and review generated summaries before using them for decisions. <br>


## Reference(s): <br>
- [Kepler MCP setup guide](references/mcp-setup.md) <br>
- [Kepler provider site](https://apisec.cn) <br>
- [ClawHub skill page](https://clawhub.ai/mylike2018/skills/kepler-agent-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown search results, article summaries, research reports, and MCP setup snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links, source labels, dates when available, and selected engine/source metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
