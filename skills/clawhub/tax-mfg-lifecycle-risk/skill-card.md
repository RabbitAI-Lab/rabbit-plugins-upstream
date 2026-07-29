## Description: <br>
A Chinese-language tax compliance assistant for manufacturing lifecycle risk self-checks covering entity setup, operations, R&D incentives, restructuring, expansion, liquidation, and related tax-risk reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask manufacturing tax-risk questions, run lifecycle self-checks, and produce structured risk and remediation guidance for Chinese tax compliance scenarios. It also provides optional MCP-based policy, risk, calculation, and knowledge-base calls plus offline reference workflows when the cloud service is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only after verifying the provider and data-handling terms, and avoid entering confidential business identities or restructuring details unless that disclosure is approved. <br>
Risk: API credentials, client identifiers, and raw query logs may be stored locally. <br>
Mitigation: Review local storage locations and retention expectations before installation, and avoid use on shared or unmanaged machines for confidential tax matters. <br>
Risk: Optional setup can alter MCP client configuration when explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode unless configuration changes have been reviewed, and inspect generated MCP entries before enabling them in enterprise environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Manufacturing lifecycle web self-check](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration] <br>
**Output Format:** [Markdown and plain text with optional JSON-style tool responses, copied reports, self-check results, and MCP configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP services for policy answers, risk checks, tax calculations, and knowledge-base metadata; offline workflows provide local reference guidance.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
