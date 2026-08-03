## Description: <br>
Provides tax invoice compliance guidance focused on digital invoice lifecycle management, shell-company false-invoice risk, recipient-side supplier screening, four-flow consistency checks, abnormal voucher response, and good-faith defense preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax staff, and compliance reviewers use this skill to structure invoice risk self-checks, supplier screening, four-flow evidence review, abnormal voucher response, and tax compliance remediation planning. It provides guidance and checklists rather than tax agency representation, filing, or guaranteed legal conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process confidential invoices, supplier data, tax disputes, or audit facts through a broader cloud tax service. <br>
Mitigation: Confirm organizational approval for remote processing before using it with sensitive tax, supplier, invoice, or audit information. <br>
Risk: The skill stores API keys, device IDs, and local plaintext logs as part of its cloud-connected client behavior. <br>
Mitigation: Review the local storage path and retention expectations before installation, and avoid use where local plaintext logs or stored credentials are not acceptable. <br>
Risk: Optional MCP setup can persist client configuration changes. <br>
Mitigation: Review proposed MCP configuration changes before enabling automatic setup or installing the skill in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-invoice-compliance) <br>
- [Interactive invoice compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_invoice_compliance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown and plain text guidance with optional command or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud tax-policy MCP service when configured; local scripts provide offline reference guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
