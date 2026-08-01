## Description: <br>
Helps renewable-resource and recycling businesses assess Chinese tax compliance risks for reverse invoicing, VAT refund eligibility, simplified taxation, documentation, and self-check reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance teams use this skill to ask renewable-resource tax questions, run preliminary risk self-checks, and generate practical compliance guidance for Chinese recycling and resource-recovery scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive business, taxpayer, invoice, or personal details may be sent to the publisher's cloud service during policy questions, risk checks, calculations, or web self-checks. <br>
Mitigation: Use non-identifying scenarios where possible, avoid regulated or confidential details unless the publisher's privacy, retention, and deletion terms are acceptable, and prefer offline reference mode for sensitive preliminary triage. <br>
Risk: The skill may create local credential, cache, health, or log files and may log user-provided question or scenario text. <br>
Mitigation: Review local data handling before deployment, restrict installation to approved environments, and clear local skill data according to organizational retention requirements. <br>
Risk: Setup behavior can detect agent clients and may write MCP configuration when explicitly enabled. <br>
Mitigation: Inspect configuration changes before enabling automatic setup and install only in environments where adding the publisher's MCP service is approved. <br>
Risk: Tax outputs are preliminary guidance and may be incomplete or stale for a specific taxpayer, locality, or filing position. <br>
Mitigation: Confirm material tax, audit, refund, or dispute decisions with current official sources and a qualified tax professional. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-renewable) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Renewable resources self-check page](https://mcp.aitaxs.top/web/topic_workflow_renewable.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax Policy Knowledge related skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and structured text responses, with optional copied self-check report text and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a publisher cloud service for policy answers, risk checks, calculations, and knowledge-base metadata; offline fallback provides limited local guidance.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
