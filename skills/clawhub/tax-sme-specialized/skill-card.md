## Description: <br>
专精特新小巨人涉税合规指引 helps enterprises and advisors self-check tax compliance for specialized SMEs, including recognition data consistency, R&D expense treatment, subsidy tax handling, listing preparation, and qualification renewal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprises, tax advisors, and compliance teams use this skill to ask China SME tax-compliance questions, run structured self-checks, prepare evidence lists, and plan remediation for specialized and innovative small giant scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and web workflow inputs may be processed by the mcp.aitaxs.top service. <br>
Mitigation: Review the service trust and retention terms before sharing confidential financial, listing-preparation, or client-identifying data. <br>
Risk: API credentials and usage logs may be stored locally by the skill's MCP client. <br>
Mitigation: Restrict local device access, review stored configuration and log locations, and rotate or delete credentials when they are no longer needed. <br>
Risk: Optional auto-setup can modify MCP client settings. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless you intend to change your MCP client configuration. <br>
Risk: The matrix installer can download related skills and modify the user's ~/.skills directory. <br>
Mitigation: Review the skill matrix before installation, use dry-run or a custom target directory when evaluating, and install only trusted related packages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-sme-specialized) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Specialized SME tax compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_sme_specialized.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with checklists, risk ratings, policy references, web workflow links, and optional command or configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP-backed answers when available, local fallback workflows when offline, and optional matrix-installation helpers for related tax skills.] <br>

## Skill Version(s): <br>
3.15.3 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
