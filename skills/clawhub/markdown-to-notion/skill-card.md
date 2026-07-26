## Description: <br>
Converts Markdown content into Notion API-compatible JSON page content by calling the XiaoBenYang remote API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content workflow users use this skill to convert Markdown into Notion API-compatible page content for publishing and integration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Markdown content is sent to the XiaoBenYang remote API. <br>
Mitigation: Use only with Markdown content appropriate for that third-party service and review data-handling requirements before use. <br>
Risk: The skill stores XBY_APIKEY in a local .env file. <br>
Mitigation: Use a scoped or disposable API key where possible and keep .env out of version control. <br>
Risk: The artifact contains unrelated Gaokao-service leftovers. <br>
Mitigation: Inspect the package before deployment and confirm the remote MCP IDs and endpoint match the intended Markdown-to-Notion workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/markdown-to-notion) <br>
- [Publisher profile](https://clawhub.ai/user/cainingnk) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [json, guidance] <br>
**Output Format:** [JSON returned from the remote API, typically summarized for the user in text or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value before API calls can succeed.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
