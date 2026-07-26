## Description: <br>
A Chinese-language assistant for construction-industry tax compliance, risk self-checks, policy Q&A, tax calculations, invoice and prepayment guidance, and remediation planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill to ask construction tax compliance questions, run self-checks, identify tax and operating risks, and generate practical remediation guidance. Developers and agents may also use its MCP and offline workflows to route tax-policy questions, risk checks, and calculations. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and self-check metrics may be sent to external services. <br>
Mitigation: Use only with non-sensitive or properly authorized data, and avoid pasting personal, payroll, bank, tax ID, or confidential business records unless the remote-service behavior has been reviewed. <br>
Risk: The skill can store service credentials and logs locally. <br>
Mitigation: Review local credential and log storage before deployment, restrict file access where appropriate, and rotate or remove credentials if the environment is shared. <br>
Risk: MCP auto-setup and matrix installation can modify local agent configuration or install additional skills into the user skills directory. <br>
Mitigation: Treat setup and installer actions as privileged, prefer dry-run mode or explicit approval, and review target paths before allowing filesystem changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [Construction compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional structured self-check results, configuration snippets, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; includes local offline fallback guidance.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
