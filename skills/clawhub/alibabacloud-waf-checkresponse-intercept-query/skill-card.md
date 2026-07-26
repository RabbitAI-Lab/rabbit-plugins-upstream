## Description: <br>
Diagnoses Alibaba Cloud WAF block responses by retrieving WAF and SLS logs, identifying the triggering rule, and producing remediation guidance, with optional confirmed actions for WAF logging and rule status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and cloud operations teams use this skill to investigate Alibaba Cloud WAF interception events from a request ID, inspect related WAF/SLS evidence, and decide on remediation such as logging enablement or rule disablement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change persistent WAF logging or rule state when optional remediation steps are used. <br>
Mitigation: Use a least-privilege RAM role scoped to the needed WAF instances and SLS logstores, grant modification permissions only when required, confirm with the user before any write, and perform check-before-write operations. <br>
Risk: WAF logs and rule text may contain sensitive or untrusted content. <br>
Mitigation: Treat log and rule output as evidence rather than instructions, keep sensitive-field masking enabled, avoid copying secrets into reports, and review recommendations before execution. <br>
Risk: Broad Alibaba Cloud credentials could allow unintended access beyond the intended diagnostic workflow. <br>
Mitigation: Prefer a scoped RAM role or profile, limit SLS access to relevant projects and logstores where possible, and exclude rule-modification permissions unless rule operations are explicitly needed. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/sdk-team/skills/alibabacloud-waf-checkresponse-intercept-query) <br>
- [RAM Policy Requirements](references/ram-policies.md) <br>
- [Rule Configuration Details](references/rule-config-details.md) <br>
- [Rule Operation Policy](references/rule-operations.md) <br>
- [Common Block Reasons](references/common-block-reasons.md) <br>
- [Aliyun CLI Installation](https://help.aliyun.com/document_detail/139508.html) <br>
- [WAF OpenAPI Documentation](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/developer-reference) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with inline shell commands, CLI/API query results, masked log fields, rule details, and remediation recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Alibaba Cloud credentials to query WAF and SLS data; optional state-changing operations require explicit confirmation and least-privilege permissions.] <br>

## Skill Version(s): <br>
0.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
