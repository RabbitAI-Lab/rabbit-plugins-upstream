## Description: <br>
Provides China-focused tax advisory practice guidance for tax service organizations, covering professional practice standards, three-level review, project delivery SOPs, service contracts, data security, risk classification, AI-enabled operations, and reusable templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax advisory firms, tax agents, accounting firms, bookkeeping agencies, and consultants use this skill to structure China tax compliance advisory workflows, draft service templates, perform self-checks, and prepare risk or remediation guidance. It is intended as AI-assisted operational guidance and template support, not a substitute for licensed professional review or official tax authority determinations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: A third-party remote tax-policy service may receive prompts or self-check metrics. <br>
Mitigation: Avoid entering confidential client, tax, contract, or regulated business data unless the organization has reviewed the endpoint, retention behavior, and data handling terms. <br>
Risk: The skill may create local credential and log files. <br>
Mitigation: Review credential and log storage before use, restrict access on shared machines, and rotate or remove credentials when no longer needed. <br>
Risk: Optional setup can modify MCP client configuration. <br>
Mitigation: Enable setup only after reviewing the proposed configuration change and keep backups of existing client configuration files. <br>
Risk: Tax guidance is policy-sensitive and may be incomplete for a specific engagement. <br>
Mitigation: Have qualified professionals verify outputs against current official sources and apply the skill's recommended human review before relying on reports or templates. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-advisory-practice) <br>
- [Tax advisory workflow self-check page](https://mcp.aitaxs.top/web/topic_workflow_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, template text, self-check results, and MCP or local workflow configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a third-party remote MCP tax-policy service and includes local offline fallback workflows.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
