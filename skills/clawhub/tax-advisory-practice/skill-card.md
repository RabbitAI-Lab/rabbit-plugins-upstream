## Description: <br>
This Chinese-language tax advisory practice skill helps tax intermediary organizations structure compliant AI-assisted service delivery, including practice standards, three-level review, consulting SOPs, tax service contracts, data security, risk grading, and staff training. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax advisory firms, accounting practices, bookkeeping agencies, and tax-service teams use this skill for Chinese-language guidance, templates, self-check workflows, and risk-control checklists for compliant tax advisory service delivery. It is intended to support human review rather than replace licensed tax professionals or firm quality-control processes. <br>

### Deployment Geography for Use: <br>
China-focused; no broader deployment restriction stated. <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send tax questions or self-check metrics to the remote mcp.aitaxs.top service. <br>
Mitigation: Avoid entering sensitive taxpayer, client, credential, or confidential financial details unless the remote-service and retention posture has been reviewed. <br>
Risk: The skill stores local API credentials and logs. <br>
Mitigation: Review the local credential and log locations before use, restrict file access, and remove or rotate credentials when the skill is no longer needed. <br>
Risk: Setup behavior can register MCP server configuration or install related skills when enabled. <br>
Mitigation: Use dry-run or explicit setup only, review generated configuration before trusting it, and install related skills only from expected publisher channels. <br>
Risk: AI-assisted tax guidance and templates can be incorrect, stale, or unsuitable for a specific engagement. <br>
Mitigation: Verify outputs against official policy sources and require qualified professional review, including the skill's stated three-level review process, before relying on advice or deliverables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-advisory-practice) <br>
- [Structured compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_advisory.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration] <br>
**Output Format:** [Markdown responses with structured checklists, templates, risk notes, and workflow links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service, local fallback workflows, local API credentials, logs, and optional client configuration when enabled.] <br>

## Skill Version(s): <br>
3.14.38 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
