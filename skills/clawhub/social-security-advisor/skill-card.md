## Description: <br>
Social Security Advisor helps users query China-focused personal social-security policy, estimate retirement and pension scenarios, compare flexible-employment contribution choices, and generate planning self-check guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer personal social-security questions, plan retirement and pension contributions, compare medical-insurance and flexible-employment options, and prepare structured self-check reports. It also offers an interactive workflow page for lightweight planning and deeper prompt handoff. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The package includes broader tax-policy MCP integration beyond the advertised personal social-security advisor. <br>
Mitigation: Install it only if you intentionally want the publisher's broader tax-policy service, and review the skill scope before enabling it. <br>
Risk: Remote service use and local persistence may affect sensitive personal, employment, medical, or business data. <br>
Mitigation: Avoid entering sensitive data unless you accept the remote service and local persistence behavior; review local configuration, cache, and log storage before use. <br>
Risk: Optional auto-setup can modify MCP client configuration files. <br>
Mitigation: Do not enable auto-setup unless you want configuration changes; review and back up client MCP configuration before enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/social-security-advisor) <br>
- [Personal social-security workflow page](https://mcp.aitaxs.top/web/topic_workflow_personal_social_security.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown and structured text with optional web workflow links, JSON-like tool results, shell commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May rely on the publisher's remote MCP service; bundled offline workflows provide limited reference and process guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
