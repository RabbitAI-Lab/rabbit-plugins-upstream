## Description: <br>
Provides Chinese-language tax advisory practice guidance for tax service firms, including professional standards, three-level review, project delivery SOPs, engagement templates, data-security controls, AI-assisted practice workflows, and compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax advisory firms, accounting practices, and compliance consultants use this skill to draft and review tax-service workflows, engagement materials, compliance checklists, self-check reports, and risk-control guidance for Chinese tax advisory practice. It supports policy Q&A, risk screening, tax calculations, MCP configuration, and offline reference workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax prompts, client-identifying details, taxpayer data, payroll records, invoice data, or confidential financial facts may be sent to remote services at mcp.aitaxs.top. <br>
Mitigation: Use the skill only when the publisher's privacy and retention terms are acceptable; minimize, redact, or anonymize sensitive client data before submission. <br>
Risk: The skill may store a local API key and supporting client state during cloud-backed MCP use. <br>
Mitigation: Review local credential handling before installation in managed environments and rotate or remove stored keys according to local policy. <br>
Risk: The initialization script can modify MCP client configuration files when explicitly run with write setup enabled. <br>
Mitigation: Do not run config/init_agent.py or enable TAX_ENABLE_AUTOSETUP unless you intentionally want it to modify MCP client configuration. <br>
Risk: Tax and compliance outputs can be incomplete, stale, or unsuitable for a specific client matter. <br>
Mitigation: Treat outputs as draft guidance; confirm policy positions against official sources and require qualified professional review before filing, signing, or advising a client. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-advisory-practice) <br>
- [Tax advisory workflow self-check page](https://mcp.aitaxs.top/web/topic_workflow_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, text responses, generated templates, JSON-like tool results, shell snippets, and MCP configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cloud-backed MCP calls may return structured tool output; offline workflows provide local reference text and process guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
