## Description: <br>
tax-steel provides metallurgy-focused tax compliance guidance, risk self-checks, policy-oriented Q&A, report templates, and practical checklists for steel, nonferrous metals, rare earth, and precious metals businesses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill to ask metallurgy tax-compliance questions, run lightweight self-checks, identify risk indicators, and draft compliance-oriented reports or remediation checklists. It is not a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check metrics may be sent to the cloud service or fallback search providers. <br>
Mitigation: Use only organization-approved data, avoid highly sensitive business details, and review the configured service endpoints before use. <br>
Risk: The skill may persist local credentials, browser credentials, and logs. <br>
Mitigation: Clear ~/.tax-policy-client and browser localStorage when credentials or logs should not remain on the machine. <br>
Risk: Optional agent auto-setup can change local agent configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes have been reviewed and approved. <br>
Risk: Tax-compliance guidance can be incomplete, outdated, or unsuitable for a specific business situation. <br>
Mitigation: Treat outputs as preliminary guidance and confirm material tax, audit, or legal decisions with qualified professionals or the relevant authority. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-steel) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Metallurgy compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_steel.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Cloud MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code, shell-command, configuration, checklist, and report-template content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud-backed MCP calls, local fallback workflows, and browser-based self-check interactions.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
