## Description: <br>
Chinese tax and equity-governance assistant for equity transfers, family holding structures, state-owned enterprise mixed-ownership reform, VIE/red-chip structures, tax burden comparisons, transaction calculations, structure design, and risk warnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax and compliance professionals, and developers use this skill to assess Chinese equity-transfer and company-governance tax scenarios, compare holding structures, run self-checks, and produce risk guidance or compliance reports. <br>

### Deployment Geography for Use: <br>
Global, with content focused on Chinese tax and equity-governance rules. <br>

## Known Risks and Mitigations: <br>
Risk: Remote service use can expose entered company or transaction details to external systems. <br>
Mitigation: Avoid entering sensitive company details unless the remote data flow is acceptable for the intended deployment. <br>
Risk: The skill can store API credentials and register a stable anonymous client identifier locally. <br>
Mitigation: Review local credential persistence before installation and rotate or remove credentials when the skill is no longer used. <br>
Risk: Client setup behavior can modify agent MCP configuration. <br>
Mitigation: Review configuration changes before enabling automatic setup and keep backups of existing MCP configuration files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Equity governance self-check page](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [artifact/SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text with optional code, shell command, configuration, and report-prompt snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include policy references, risk levels, calculations, self-check report prompts, and remediation checklists.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
