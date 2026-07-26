## Description: <br>
Cross-tool golden rules for an autonomous Scrapfly web agent connected to the Scrapfly MCP server (web_scrape, screenshot, extract, classify_block, the Cloud Browser lifecycle, snapshot/click/fill/type/press/scroll/select/drag, and WebMCP). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scrapfly](https://clawhub.ai/user/scrapfly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an LLM agent is connected to the Scrapfly MCP server and needs guidance for choosing between stateless scraping, stateful Cloud Browser interaction, unblocking flows, WebMCP calls, and alert setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent operating a browser through logged-in sessions and may expose or rely on a Scrapfly API key. <br>
Mitigation: Install only for trusted publishers, store and rotate SCRAPFLY_API_KEY carefully, and require explicit confirmation before purchases, account changes, messages, or other sensitive website actions. <br>
Risk: Browser automation can mutate live page state, causing stale snapshots or unintended actions if multiple browser tools run at once. <br>
Mitigation: Follow the skill's one-tool-per-turn and post-mutation snapshot guidance before choosing the next browser action. <br>


## Reference(s): <br>
- [Scrapfly MCP endpoint](https://mcp.scrapfly.io/mcp) <br>
- [Scrapfly agent reference bootstraps](https://github.com/scrapfly/agent-ai) <br>
- [ClawHub skill page](https://clawhub.ai/scrapfly/skills/scrapfly-agent-rules) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and decision rules] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing operational guidance for Scrapfly MCP tool selection, browser session handling, unblocking, snapshots, WebMCP usage, and alert workflow sequencing.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
