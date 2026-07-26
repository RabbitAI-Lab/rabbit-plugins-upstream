## Description: <br>
Read GitHub helps agents inspect GitHub repository documentation and code through gitmcp.io instead of raw scraping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to fetch, search, and navigate GitHub repository documentation and code when answering questions about a project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote requests through gitmcp.io and broad fetch-url or direct call commands can expose the agent to untrusted content or unexpected external tool behavior. <br>
Mitigation: Prefer the scoped fetch-docs, search-docs, and search-code commands; use fetch-url and direct call only for trusted targets after review. <br>
Risk: The security evidence marks the skill suspicious because its remote tool-calling powers are broader than a normal repository reader needs. <br>
Mitigation: Review and scan the skill before deployment, and monitor use for arbitrary external URLs or unnecessary direct MCP tool calls. <br>


## Reference(s): <br>
- [Read GitHub on ClawHub](https://clawhub.ai/am-will/skills/read-github) <br>
- [gitmcp.io](https://gitmcp.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Repository content is retrieved through gitmcp.io MCP tools; broader URL fetches and direct tool calls should be used only for trusted targets.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
