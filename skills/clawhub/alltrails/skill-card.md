## Description: <br>
This skill provides read-only AllTrails trail search, trail details, reviews, photos, weather, GPX export, and signed-in user list and activity access through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask agents for AllTrails hiking and trail information, including trail discovery, reviews, photos, weather, GPX route data, and their own saved or completed trails when signed in. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server can read AllTrails data available in the user's signed-in browser session, including account-scoped activity. <br>
Mitigation: Install and use it only when that session access is acceptable, and reserve account-scoped tools for profile, saved list, completed trail, or activity feed requests. <br>
Risk: The skill relies on an unofficial internal AllTrails API and may carry Terms of Service and reliability risk. <br>
Mitigation: Review AllTrails Terms of Service before use and expect the integration to break if AllTrails changes or blocks the underlying internal API. <br>


## Reference(s): <br>
- [AllTrails MCP npm package](https://www.npmjs.com/package/alltrails-mcp) <br>
- [AllTrails MCP source repository](https://github.com/chrischall/alltrails-mcp) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only AllTrails data responses may include trail details, reviews, photos, weather, GPX route data, profile details, saved lists, completed trails, and activity feed summaries.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
