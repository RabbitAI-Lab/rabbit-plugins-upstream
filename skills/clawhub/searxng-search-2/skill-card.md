## Description: <br>
Provides web search capability for agents through an MCP server backed by a configurable SearXNG endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zfanmy](https://clawhub.ai/user/zfanmy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent query a configured SearXNG instance and return web search results through MCP or a shell wrapper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the configured SearXNG endpoint. <br>
Mitigation: Use a trusted SearXNG instance, preferably over HTTPS for remote servers, and avoid searching secrets or confidential project data. <br>
Risk: Copying the included mcporter configuration can replace an existing local configuration. <br>
Mitigation: Merge or back up existing mcporter config before copying this package's config.json. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zfanmy/skills/searxng-search-2) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Text, Markdown, or JSON search results with MCP tool responses and shell usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SEARXNG_URL to point to the SearXNG instance used for searches.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
