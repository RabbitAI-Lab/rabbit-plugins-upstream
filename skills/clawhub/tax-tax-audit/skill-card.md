## Description: <br>
企业财税合规审计与税务审计专项助手，帮助用户梳理财务报表审计中的税务法规考虑、税务内控测试、涉税舞弊识别、关键审计事项披露和税务合规自检。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Auditors, tax professionals, and compliance teams use this skill to structure tax-audit procedures, identify tax-control and fraud indicators, draft disclosure language, and produce self-check guidance for Chinese enterprise tax compliance scenarios. <br>

### Deployment Geography for Use: <br>
Global, with content focused on Chinese tax audit and compliance workflows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax or audit content to cloud service paths. <br>
Mitigation: Use it only when cloud processing is approved, and avoid sending client-identifying or confidential tax facts unless the data has been cleared for that service path. <br>
Risk: The skill can store service keys for authenticated service access. <br>
Mitigation: Protect local configuration files, avoid sharing generated keys, and rotate or remove keys when access is no longer needed. <br>
Risk: The full matrix installer and automatic setup can install additional skills or persist MCP configuration. <br>
Mitigation: Run the matrix installer or enable TAX_ENABLE_AUTOSETUP only when those configuration changes and additional skill installs are intentional. <br>
Risk: The server security verdict requires review before deployment. <br>
Mitigation: Review and scan the skill before deployment, especially for environments that handle confidential audit, tax, or client information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-audit) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [国家税务总局官网](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional JSON-style tool results and command/configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce checklists, risk indicators, audit procedure outlines, disclosure templates, local setup guidance, and offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
