## Description: <br>
网络研究助手 provides web search, page crawling, package and repository research, documentation lookup, image search, and related web-research tools through the Xiaobenyang service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to gather fresh web results, retrieve page text, evaluate packages or repositories, find examples, compare technologies, and check service status. It is most appropriate when externally sourced research results are useful and the user can decide what context is safe to send to the Xiaobenyang service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries, URLs, stack traces, package names, and other submitted context are sent to an external Xiaobenyang service. <br>
Mitigation: Install only if that service is trusted for the intended data, and avoid sending private internal links, secrets, tokens, proprietary logs, or sensitive user data. <br>
Risk: The required API key is stored in a local plaintext .env file. <br>
Mitigation: Use a scoped or revocable API key, keep the .env file out of source control and backups where possible, and rotate the key if it may have been exposed. <br>
Risk: Cloud-backed research results can be incomplete, stale, or misleading. <br>
Mitigation: Review returned sources and outputs before relying on them for decisions, citations, or code changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/xby-web-research-assistant) <br>
- [Xiaobenyang API key and service site](https://xiaobenyang.com) <br>
- [Xiaobenyang MCP service endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown summaries with structured JSON-derived results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Xiaobenyang API key; outputs may include externally retrieved web, package, repository, image, documentation, and service-status data.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
