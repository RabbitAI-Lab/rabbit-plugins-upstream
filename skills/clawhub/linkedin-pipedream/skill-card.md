## Description: <br>
Post to LinkedIn, comment, like, search organizations, and manage profiles via Pipedream OAuth integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g9pedro](https://clawhub.ai/user/g9pedro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect LinkedIn through Pipedream OAuth, then draft commands and helper-script usage for posting, commenting, liking, organization search, profile lookup, and post deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored Pipedream credentials and hardcoded account identifiers could target the wrong LinkedIn user, organization, or auth provision. <br>
Mitigation: Install only for controlled LinkedIn and Pipedream accounts, replace all sample Telegram, member, organization, and auth provision IDs with verified values, and keep ~/.config/pdauth/config.json out of committed or shared material. <br>
Risk: The skill can post, comment, like, or delete public LinkedIn content. <br>
Mitigation: Require explicit confirmation before publishing, engaging with, or deleting content, and verify account access with pdauth status before executing actions. <br>
Risk: Organization posting uses a direct SDK workaround because the documented MCP organization tools are broken. <br>
Mitigation: Review the helper script and organization admin access before use, then run it only with intended organization IDs and post text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g9pedro/skills/linkedin-pipedream) <br>
- [Pipedream MCP](https://mcp.pipedream.com) <br>
- [LinkedIn API Docs](https://learn.microsoft.com/en-us/linkedin/marketing/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JavaScript helper code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires pdauth and a connected LinkedIn account through Pipedream OAuth.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
