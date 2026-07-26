## Description: <br>
Monetize an MCP server or agent tool you're building or maintaining with disclosed sponsored slots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lulu-the-narwhal](https://clawhub.ai/user/lulu-the-narwhal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and maintainers use this skill to add Lulu Ads sponsored slots to MCP servers or agent tools, including publisher registration, SDK setup, credential handling, and integration verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The integration may register a publisher account and send registration fields to Lulu. <br>
Mitigation: Ask the human for explicit approval before creating a publisher account or submitting registration data. <br>
Risk: The integration stores Lulu credentials for runtime use. <br>
Mitigation: Store the publisher ID and API key in environment variables and never hardcode the API key in source files. <br>
Risk: Persistent agent guidance can preserve monetization behavior across future edits. <br>
Mitigation: Add persistent guidance only after the human confirms they want the sponsored-slot behavior maintained. <br>
Risk: Sponsored content could be attached in contexts where the skill says it should not appear. <br>
Mitigation: Do not attach sponsored content to error responses, and do not add instructions telling the host or model to display the sponsored field. <br>


## Reference(s): <br>
- [Lulu Ads MCP endpoint](https://ads.getlulu.dev/mcp) <br>
- [Lulu publisher signup](https://getlulu.dev/publishers) <br>
- [Lulu Ads documentation](https://getlulu.dev/docs.md) <br>
- [Lulu Ads installation reference](https://ads.getlulu.dev/install.md) <br>
- [ClawHub skill page](https://clawhub.ai/lulu-the-narwhal/skills/lulu-ads) <br>
- [Publisher profile](https://clawhub.ai/user/lulu-the-narwhal) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell, Python, TypeScript, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose dependency installation, environment variables, SDK calls, MCP configuration, and verification steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
