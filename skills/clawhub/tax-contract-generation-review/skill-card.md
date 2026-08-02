## Description: <br>
A contract generation and review assistant for enterprise contract templates, clause review, tax-risk checks, compliance review reports, and contract lifecycle guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise legal, compliance, finance, tax, and management users can use this skill to find or draft contract templates, review clauses for legal and tax concerns, identify common contract risk indicators, and produce review guidance. The skill is especially oriented toward Chinese business contract workflows and tax-compliance checks. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may contact mcp.aitaxs.top and register or use API credentials for remote MCP-backed policy, risk, invoice, and report services. <br>
Mitigation: Review the remote-service data flow before installation, restrict network access if remote calls are not acceptable, and use offline workflows where possible. <br>
Risk: The skill may create and store local API credentials and logs, including some prompts or scenarios in plaintext. <br>
Mitigation: Avoid entering confidential contracts, personal data, or sensitive business terms unless local storage and retention have been reviewed; periodically inspect and clear local client data if required by policy. <br>
Risk: Setup code can modify MCP client configuration when explicitly run or enabled. <br>
Mitigation: Run setup in dry-run mode first, review proposed MCP configuration changes, and back up or version user MCP configuration before enabling automatic setup. <br>
Risk: Contract and tax outputs may be incomplete or jurisdiction-sensitive. <br>
Mitigation: Treat generated contract clauses, tax analysis, and review reports as drafting support that should be checked by qualified legal, tax, or compliance reviewers before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Hosted contract compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional code, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate contract templates, clause-review findings, compliance checklists, risk classifications, tax guidance, report-style summaries, and setup guidance for remote or local MCP access.] <br>

## Skill Version(s): <br>
3.15.7 (source: ClawHub release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
