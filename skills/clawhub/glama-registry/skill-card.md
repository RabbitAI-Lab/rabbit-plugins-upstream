## Description: <br>
Searches MCP registry data for servers matching a query string and returns matching server results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to look up MCP servers by keyword and present matching registry results to users. It requires a XiaoBenYang API key before making registry queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file in plaintext. <br>
Mitigation: Use a dedicated, low-privilege API key and remove the .env entry when the skill is no longer needed. <br>
Risk: The security summary flags inconsistent copied documentation as a documentation quality warning. <br>
Mitigation: Review the skill before installing and rely on the documented MCP registry search behavior only after confirming it matches the intended use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alinklab/skills/glama-registry) <br>
- [XiaoBenYang API key page](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a query string and an XBY_APIKEY provided by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; SKILL.md frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
