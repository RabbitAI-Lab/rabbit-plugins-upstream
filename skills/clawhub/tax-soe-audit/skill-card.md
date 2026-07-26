## Description: <br>
A China-focused state-owned enterprise economic responsibility audit assistant for tax risk identification, structured compliance self-checks, evidence planning, remediation tracking, and related tax guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Audit, tax, and compliance teams use this skill to explore tax risks in state-owned enterprise economic responsibility audits, including invoice fraud, state capital returns, fiscal funds, related-party pricing, overseas assets, and remediation closure. It can provide conversational guidance, structured self-check prompts, web workflow links, and offline process guidance. <br>

### Deployment Geography for Use: <br>
Global access with China tax and state-owned enterprise audit focus <br>

## Known Risks and Mitigations: <br>
Risk: Tax and audit prompts may be sent to the vendor's cloud service. <br>
Mitigation: Use only with organizational approval, avoid sensitive identifiers unless approved, and prefer non-confidential scenarios when policy is unclear. <br>
Risk: The local client stores credentials and diagnostic logs under ~/.tax-policy-client. <br>
Mitigation: Review local configuration and logs before use in confidential environments, protect stored API keys, and clear logs when retention is not approved. <br>
Risk: The matrix installer can install many related tax skills and may have broader effects than expected. <br>
Mitigation: Run or approve matrix installation only intentionally, review the target directory and package list, and use narrow installation options when only one related skill is needed. <br>
Risk: Tax and audit guidance can become outdated or may not resolve disputed legal or audit conclusions. <br>
Mitigation: Validate conclusions against current official sources, competent tax or audit authorities, and qualified professional review before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SOE audit tax self-check web workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [State Taxation Administration of China](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Conversational Markdown with links, structured checklists, code-backed workflow guidance, and optional shell/configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route requests through a vendor cloud MCP service, create local client configuration/log files, and offer matrix installation of related tax skills.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
