## Description: <br>
Tax Restructuring assists with Chinese tax guidance, risk checks, calculations, and compliance workflows for bankruptcy restructuring, listed-company restructuring, mergers, divisions, debt restructuring, asset transfers, and cross-border restructuring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance professionals use this skill to get restructuring-tax answers, risk warnings, self-check guidance, and operational checklists for Chinese enterprise restructuring and capital transactions. The skill can also route tax questions to remote MCP services and provide offline fallback guidance when those services are unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check metrics may leave the local environment for mcp.aitaxs.top, with possible fallback searches to Bing or Baidu. <br>
Mitigation: Avoid regulated or confidential inputs unless this network behavior is acceptable, and prefer publisher changes that disable ungated public-search fallback for sensitive deployments. <br>
Risk: The security summary flags under-disclosed local persistence and agent-configuration behavior, including local storage of API credentials and query logs. <br>
Mitigation: Review the security notice before installation, avoid setup scripts or TAX_ENABLE_AUTOSETUP in controlled environments, and require clearer privacy disclosures before production rollout. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [Restructuring tax self-check page](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Security and privacy notice](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown and JSON-like tool results with optional shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for tax policy answers, risk checks, tax calculations, and knowledge-base listings; includes local offline reference workflows.] <br>

## Skill Version(s): <br>
3.15.11 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
