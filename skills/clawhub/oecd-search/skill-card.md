## Description: <br>
Provides agent tools for finding OECD datasets, inspecting dataset structures, querying observations, and generating OECD Data Explorer URLs through a third-party MCP API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to search OECD statistical datasets, inspect dataflow metadata, retrieve selected observations, and produce browser links for further exploration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an XBY/xiaobenyang API key and saves it in a local .env file. <br>
Mitigation: Use a limited or revocable key when available, keep .env out of shared repositories, and install only where local credential storage is acceptable. <br>
Risk: OECD-style queries are routed through a third-party hosted XBY MCP service rather than a direct OECD-only integration. <br>
Mitigation: Treat returned data as third-party service output and verify high-impact results against authoritative OECD sources before relying on them. <br>
Risk: Broad data queries can produce large responses that may exceed an agent context window. <br>
Mitigation: Use dataset filters, start and end periods, or last_n_observations; keep result sets within the documented maximum of 1000 observations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/oecd-search) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown summaries with raw JSON data and generated URLs from tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value; data queries default to the last 100 observations and should be constrained with filters, dates, or last_n_observations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
