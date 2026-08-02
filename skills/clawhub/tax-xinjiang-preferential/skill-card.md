## Description: <br>
Provides Xinjiang regional tax-preference guidance, eligibility checks, risk self-assessment, and landing-planning support for preferential corporate income tax regimes, local-share exemptions, bonded-zone operating models, and branch tax treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, tax teams, and advisors use this skill to evaluate Xinjiang regional tax-preference eligibility, compare preferential regimes, prepare evidence checklists, and generate preliminary compliance self-check guidance. It is advisory and should be verified against official tax authority requirements and qualified professionals for filing or legal decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenario details may be sent to mcp.aitaxs.top for remote MCP processing. <br>
Mitigation: Use only if the publisher's privacy and retention terms are acceptable; avoid confidential tax, financial, identity, or business details unless disclosure has been approved. <br>
Risk: The package stores service credentials locally for MCP access. <br>
Mitigation: Install in an environment with appropriate file permissions, review local credential storage before use, and remove stored credentials when the skill is no longer needed. <br>
Risk: Optional auto-setup can modify MCP client configuration files when explicitly enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless configuration changes are intended; inspect the generated MCP configuration and backups before relying on the setup. <br>
Risk: Tax calculations, eligibility conclusions, and risk scores are advisory and may be wrong or stale for a specific taxpayer. <br>
Mitigation: Verify material conclusions against official tax authority guidance and qualified tax or legal professionals before filing, restructuring, or claiming incentives. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-xinjiang-preferential) <br>
- [Xinjiang preferential tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_xinjiang_preferential.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, shell commands] <br>
**Output Format:** [Markdown and structured text with optional web self-check results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; local fallback output is preliminary process guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
