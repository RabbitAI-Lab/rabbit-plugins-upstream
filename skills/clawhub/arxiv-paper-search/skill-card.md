## Description: <br>
Searches arXiv papers, retrieves PDF links, and parses paper content for academic and AI research workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and developer agents use this skill to find arXiv papers, retrieve PDF URLs, and parse paper content for review or summarization. It is especially oriented toward current AI and academic paper discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the XBY/Xiaobenyang API key and paper requests to a third-party MCP service. <br>
Mitigation: Use a dedicated key, install only in workspaces where that service is acceptable, and limit calls to the intended arXiv tools. <br>
Risk: The skill stores the API key in a local .env file. <br>
Mitigation: Avoid shared or sensitive workspaces, restrict file access, or modify the skill to avoid persistent key storage. <br>
Risk: Paper queries, arXiv IDs, and raw responses may pass through mcp.xiaobenyang.com. <br>
Mitigation: Do not submit sensitive research queries, and redact raw responses before sharing them outside the workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/arxiv-paper-search) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP service](https://mcp.xiaobenyang.com) <br>
- [arXiv](https://arxiv.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [JSON tool results summarized as text or Markdown for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY/Xiaobenyang API key and calls a third-party MCP service.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
