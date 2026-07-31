## Description: <br>
A tax restructuring assistant that helps users analyze China-focused enterprise restructuring and capital transaction tax issues, including bankruptcy restructuring, listed-company restructuring, mergers, divisions, debt restructuring, cross-border restructuring, tax deferral, and risk warnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and compliance teams use this skill to obtain structured guidance, risk checks, tax calculations, and self-check report material for enterprise restructuring and capital transaction scenarios. The subject matter is centered on China tax policy and restructuring compliance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send restructuring, tax, or transaction questions to a cloud-backed MCP service, and fallback behavior may use public search. <br>
Mitigation: Avoid entering confidential transaction facts unless the deployment has approved the remote service and fallback behavior; use offline guidance for preliminary review when sensitive details cannot leave the environment. <br>
Risk: The skill can store API keys, identifiers, health state, and query or scenario logs locally. <br>
Mitigation: Run it only on trusted workstations, restrict access to the local client data directory, and periodically review or clear stored configuration and logs under the tax policy client data location. <br>
Risk: Optional setup can modify MCP client configuration. <br>
Mitigation: Keep automatic setup disabled unless intended, review any proposed MCP configuration change before enabling it, and use backups or change control for managed client environments. <br>
Risk: Tax restructuring guidance may be incomplete or time-sensitive for a specific transaction. <br>
Mitigation: Verify conclusions against current official tax guidance and qualified tax or legal professionals before filing, restructuring, or relying on a material tax position. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [Tax restructuring self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text, structured tool results, Python helper code, shell commands, and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud-backed MCP tools for policy questions, risk checks, calculations, and knowledge-base listings, with local fallback guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
