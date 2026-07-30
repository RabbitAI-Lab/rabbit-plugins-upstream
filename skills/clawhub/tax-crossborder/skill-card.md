## Description: <br>
Provides China-focused cross-border e-commerce and trade tax compliance guidance, risk self-checks, tax calculations, and report templates for import, export, withholding tax, indirect equity transfer, CRS, foreign tax credit, beneficial owner, VIE/red-chip, and Hainan Free Trade Port scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, compliance, and trade operations users use this skill for preliminary cross-border tax policy Q&A, compliance self-checks, risk triage, tax calculations, and drafting practical checklists or self-assessment reports. Outputs are advisory aids and should be reviewed against official policy and professional judgment before filing or enforcement decisions. <br>

### Deployment Geography for Use: <br>
Global, with China-focused cross-border tax content. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, company, transaction, or personal data may be sent to remote services during policy Q&A, risk checks, or calculations. <br>
Mitigation: Review before installing, redact confidential inputs where possible, and only use remote-service features when the data handling is acceptable for the user's environment. <br>
Risk: The artifact can create persistent local identifiers, configuration, cache, and log files. <br>
Mitigation: Inspect local data under the skill's client directory, avoid use on shared machines for confidential matters, and clear local identifiers or logs when they are no longer needed. <br>
Risk: Automatic MCP setup can change local client configuration when explicitly enabled. <br>
Mitigation: Keep automatic setup disabled unless reviewed; inspect proposed MCP configuration changes before enabling setup or setting TAX_ENABLE_AUTOSETUP. <br>
Risk: Tax calculations, risk scoring, and policy guidance may be incomplete, outdated, or unsuitable for a specific case. <br>
Mitigation: Treat outputs as preliminary guidance, verify against official sources, and consult qualified tax or legal professionals for filing, audit, dispute, or high-value decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Cross-border compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown responses and JSON-like structured tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy answers, risk levels, tax calculations, checklists, compliance report text, and MCP configuration guidance.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
