## Description: <br>
A Model Context Protocol data skill that provides real-time and historical NBA data, including player statistics, game scores, team information, and advanced analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to answer NBA data questions by resolving teams, players, games, schedules, standings, box scores, player statistics, and advanced metrics through the XiaoBenYang MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a XiaoBenYang API key and stores it in plaintext in a local .env file. <br>
Mitigation: Use a dedicated revocable key, restrict access to the workspace, and prefer a revised release that avoids plaintext secret persistence and documents key deletion or revocation. <br>
Risk: Requests and API-key-authenticated traffic are sent through mcp.xiaobenyang.com. <br>
Mitigation: Install only when the user accepts that provider trust boundary and avoid sending sensitive prompts or data through the service. <br>
Risk: Stale Gaokao copy-paste references may confuse setup or review even though the skill is for NBA data. <br>
Mitigation: Review the NBA-specific tool list and configuration before deployment, and prefer a cleaned release with the leftover references removed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/nba-stats) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration guidance] <br>
**Output Format:** [Markdown summaries derived from JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value; tool functions return success status, raw JSON data, and a message.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
