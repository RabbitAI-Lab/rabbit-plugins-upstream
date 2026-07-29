## Description: <br>
Assists with tax-risk and compliance workflows for state-owned enterprise economic responsibility audits, including invoice and off-book-account checks, state capital revenue, earmarked fiscal funds, major tax decisions, overseas asset tax, and remediation closure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, compliance, and audit users use this skill to triage state-owned enterprise audit tax risks, run structured self-check workflows, generate report prompts, and obtain policy-oriented Q&A or calculation guidance. It is oriented to Chinese tax and audit compliance scenarios and should be reviewed before use with real taxpayer, procurement, or internal-control data. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the skill under-discloses remote data flows, local credential storage, logging, and optional client configuration changes. <br>
Mitigation: Review service, logging, credential storage, and client configuration behavior before installing in environments that handle real audit, taxpayer, procurement, or internal-control data. <br>
Risk: The skill is cloud-connected and may send user scenarios to a remote tax-policy service. <br>
Mitigation: Avoid entering confidential case details unless the remote service terms, retention, access controls, and organizational approval are confirmed. <br>
Risk: The artifact includes optional client configuration setup and local API-key/config storage. <br>
Mitigation: Keep automatic setup disabled unless approved, inspect generated MCP configuration before enabling it, and manage stored credentials according to organizational policy. <br>
Risk: The skill provides tax and audit guidance in a time-sensitive regulatory area and states that final determinations depend on competent authorities. <br>
Mitigation: Verify outputs against current official tax and audit sources and obtain qualified review before filing, remediation, or enforcement decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [SOE audit self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain-text guidance, copied report prompts, JSON-like MCP tool responses, and Python CLI output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline workflows provide local checklist and reference output.] <br>

## Skill Version(s): <br>
3.15.4 (source: evidence.release.version and SKILL.md frontmatter; changelog dated 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
