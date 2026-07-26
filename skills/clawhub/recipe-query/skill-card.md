## Description: <br>
一个支持通过命令行查询菜谱和报菜名的菜谱查询工具，适用于烹饪爱好者和开发者。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, cooking enthusiasts, and developers use this skill to list available dishes and retrieve recipe content by dish name through a command-line agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports persistent plaintext API-key handling in a local .env file. <br>
Mitigation: Use a secure secret store or non-persistent credential entry, and ensure .env files are not committed or shared. <br>
Risk: The security scan reports mismatched gaokao-related configuration in a recipe lookup skill. <br>
Mitigation: Review the configured backend, MCP identifiers, and data sent to the API before installation or use. <br>
Risk: The skill may contact an external API service to complete recipe queries. <br>
Mitigation: Confirm the external service is acceptable for the intended environment and avoid sending sensitive user data in recipe requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/recipe-query) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown summary of API JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY credential and may contact the XiaoBenYang API service.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
