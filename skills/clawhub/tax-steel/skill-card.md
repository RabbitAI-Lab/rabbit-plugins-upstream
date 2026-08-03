## Description: <br>
Provides metallurgy-sector tax compliance guidance, self-check workflows, calculations, and report-oriented assistance for steel, non-ferrous metals, rare earth, and precious metals scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax-compliance teams use this skill to ask metallurgy-industry tax questions, run structured risk self-checks, compare policy-driven indicators, and draft practical compliance analysis for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions, scenarios, or selected self-check metrics to mcp.aitaxs.top. <br>
Mitigation: Use it only where that cloud data flow is approved, and avoid entering confidential company identifiers unless the organization has authorized the disclosure. <br>
Risk: The package stores a local API key and includes optional MCP client auto-setup behavior. <br>
Mitigation: Review or disable installer and configuration scripts before execution, and protect or remove local credentials according to organizational policy. <br>
Risk: Tax calculations, risk scores, and compliance recommendations are advisory and may not reflect every jurisdictional or case-specific requirement. <br>
Mitigation: Have qualified tax, audit, or legal professionals validate conclusions before filings, disputes, or material business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-steel) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Metallurgy compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_steel.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell command, configuration, and report snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud-backed MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; includes local offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
