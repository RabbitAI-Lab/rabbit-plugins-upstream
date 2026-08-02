## Description: <br>
Provides compliance planning guidance for Chinese resident individuals with overseas securities, deposits, property, or financial accounts, covering tax reporting, foreign tax credits, compliant investment channels, foreign-exchange registration, tax residency rules, and CRS consistency checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, Chinese resident individuals with overseas assets, and tax advisers use this skill to assess overseas-income reporting, creditability of foreign tax paid, compliant investment channels, CRS consistency, and remediation priorities. It provides guidance and self-check workflows, not tax filing, legal representation, or professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check data may be sent to mcp.aitaxs.top. <br>
Mitigation: Review the publisher and data flow before installation, and avoid entering identifiable financial details unless that remote processing is acceptable. <br>
Risk: API keys and client identifiers may be stored locally. <br>
Mitigation: Treat local client configuration as sensitive and review stored credentials before sharing machines, logs, or backups. <br>
Risk: Auto-setup behavior can modify local MCP client configuration when enabled. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run setup scripts unless you intend to add this MCP service to local client configuration. <br>
Risk: The security summary flags broader remote-service, credential, search, and setup behaviors beyond the advertised personal overseas investment purpose. <br>
Mitigation: Limit use to the intended tax self-check and guidance workflow, and review the artifact before deployment in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Personal overseas investment self-check page](https://mcp.aitaxs.top/web/topic_workflow_individual_overseas.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and structured JSON-style responses with optional configuration snippets and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for policy questions, risk checks, tax calculations, and knowledge-base metadata; offline fallback provides local reference guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
