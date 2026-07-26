## Description: <br>
Alibaba Cloud PolarDB Database AI Assistant supports PolarDB MySQL and PostgreSQL cluster management, inspection, performance diagnostics, parameter explanation, SQL and log analysis, backup checks, security review, high availability review, event analysis, and related PolarDB operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database operators use this skill to route PolarDB operational questions through Alibaba Cloud's Yaochi Agent, using existing aliyun CLI credentials for diagnostics, inspection, parameter explanation, and evidence-driven troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the configured Alibaba Cloud CLI identity for PolarDB diagnostics, and the required CLI/plugin setup may be broader than the PolarDB-only scope. <br>
Mitigation: Use a least-privilege RAM user or temporary credentials limited to the required Yaochi Agent and PolarDB read-only permissions, and avoid broad role profiles. <br>
Risk: Diagnostic prompts, logs, SQL text, or backend responses may contain sensitive operational data. <br>
Mitigation: Do not paste secrets, full SQL dumps, sensitive logs, or unrelated production data into queries; share only the minimum evidence needed for the diagnostic task. <br>
Risk: The installation flow asks users to review and run a CLI installer and enable or update Alibaba Cloud CLI plugins. <br>
Mitigation: Review downloaded installers before execution, enable only required plugins, and avoid unrelated plugin changes unless they are needed for the PolarDB workflow. <br>
Risk: The skill may provide guidance for high-impact operations such as parameter changes, failover, recovery, whitelist changes, or backup actions. <br>
Mitigation: Require explicit user confirmation before any high-risk action path, verify recovery point and business impact, and rely only on backend-returned evidence for operational status or completion claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-polardb-ai-assistant) <br>
- [Aliyun CLI installation guide](references/cli-installation-guide.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [RAM policies](references/ram-policies.md) <br>
- [Verification method](references/verification-method.md) <br>
- [Acceptance criteria](references/acceptance-criteria.md) <br>
- [Alibaba Cloud RAM authorization documentation](https://help.aliyun.com/document_detail/116146.html) <br>
- [Alibaba Cloud CLI documentation](https://help.aliyun.com/zh/cli/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and structured diagnostic guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include streamed diagnostic text from Yaochi Agent and a session ID for multi-turn follow-up.] <br>

## Skill Version(s): <br>
0.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
