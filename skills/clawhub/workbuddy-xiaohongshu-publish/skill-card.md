## Description: <br>
Publishes notes, Markdown, or HTML content as Xiaohongshu image posts through a macOS-focused local Chrome workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[a-persimmons](https://clawhub.ai/user/a-persimmons) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content operators use this skill to convert notes, Markdown, or HTML into vertical Xiaohongshu card images and publish them through a local Chrome session after user review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow stores active Xiaohongshu account cookies in cookies.json in a local work directory. <br>
Mitigation: Treat cookies.json like a password: keep it outside shared project folders, restrict permissions, and delete or rotate it after use. <br>
Risk: The workflow runs a persistent local publishing service for account automation. <br>
Mitigation: Avoid leaving the MCP service running when not publishing and confirm only the intended local service is active. <br>
Risk: Published Xiaohongshu posts cannot be edited or deleted through the MCP workflow. <br>
Mitigation: Review rendered cards and content carefully and require explicit user confirmation before publishing. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/a-persimmons/workbuddy-xiaohongshu-publish) <br>
- [ClawHub skill page](https://clawhub.ai/a-persimmons/skills/workbuddy-xiaohongshu-publish) <br>
- [xiaohongshu-mcp releases](https://github.com/xpzouying/xiaohongshu-mcp/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces publishing workflow instructions, local file conventions, and user-confirmation guidance before publish.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
