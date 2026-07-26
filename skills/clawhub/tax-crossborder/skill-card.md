## Description: <br>
Assists with cross-border e-commerce and trade tax compliance self-checks, risk triage, tax calculation guidance, export refund documentation, foreign exchange compliance, withholding tax, CRS, foreign tax credits, beneficial ownership, Hainan Free Trade Port topics, and VIE or red-chip structure tax risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask cross-border trade tax questions, run lightweight compliance self-checks, identify tax and customs risk indicators, and prepare practical remediation guidance for Chinese tax and cross-border business scenarios. <br>

### Deployment Geography for Use: <br>
China and cross-border transactions involving Chinese tax compliance <br>

## Known Risks and Mitigations: <br>
Risk: Tax scenarios and compliance details may be sent to a remote tax service. <br>
Mitigation: Use the skill only after accepting remote-processing risk, and redact confidential tax, financial, personal, or corporate-structure details before use. <br>
Risk: The skill can register and store persistent API credentials. <br>
Mitigation: Review credential storage before deployment, restrict access to the local configuration directory, and remove stored credentials when the skill is no longer needed. <br>
Risk: The skill can probe local agent or client setup and install or update related skills. <br>
Mitigation: Review installation and client-configuration changes before enabling auto-setup or matrix installation, and run installation steps in a controlled environment. <br>
Risk: Tax calculations, compliance flags, and remediation suggestions may be incomplete or jurisdiction-sensitive. <br>
Mitigation: Treat outputs as decision support, verify against official tax authority guidance, and consult qualified tax or legal professionals for filings, audits, disputes, or high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Cross-border compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax policy knowledge hub](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance, JSON-like risk results, Python scripts, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools, a local stdio proxy, local fallback workflows, and a web self-check page.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
