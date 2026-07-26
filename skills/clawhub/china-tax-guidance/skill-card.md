## Description: <br>
办税合规智能指引 helps enterprise tax staff navigate China electronic tax bureau workflows, filing paths, invoice handling, deregistration, credit repair, tax calendars, forms, and common compliance questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and enterprise tax or finance staff use this skill to obtain practical guidance for China tax registration, electronic filing, invoice workflows, tax deregistration, credit repair, forms, deadlines, and related operational questions. It provides guidance and checklists, but users remain responsible for filing, payment, authentication, and professional tax or legal decisions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and calculation inputs may be sent to mcp.aitaxs.top, and fallback searches may use Bing or Baidu. <br>
Mitigation: Avoid entering personal identifiers, credentials, or confidential business details unless the publisher's data handling and retention practices are acceptable. <br>
Risk: The security evidence reports local storage of an API key, device id, cache, health files, and logs under ~/.tax-policy-client. <br>
Mitigation: Review local storage on shared or managed systems, protect any API key, and clear local cache or logs when they are no longer needed. <br>
Risk: The skill can generate or merge MCP client configuration when auto-setup is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended, and inspect generated MCP client configuration before use. <br>
Risk: The authoritative security verdict is suspicious because of under-disclosed remote service, credential, logging, search, and host-configuration behavior. <br>
Mitigation: Review the skill and scan results before deployment, and limit use to environments where those behaviors are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Publisher profile: zxj2devs](https://clawhub.ai/user/zxj2devs) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [China State Taxation Administration](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, configuration] <br>
**Output Format:** [Markdown or structured text guidance with optional checklists and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may rely on remote tax-policy MCP tools, local fallback workflows, and user-provided tax scenarios.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
