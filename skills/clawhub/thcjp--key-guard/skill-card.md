## Description:

密钥卫士 provides agent guidance for detecting, masking, and reporting API-key exposure risks before requests or configuration content are sent to an AI assistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and automation teams use this skill to have an agent inspect API-key-related request content, configuration references, and scripts, then produce masked status information, risk notes, and remediation guidance. It is not intended for unauthorized penetration testing or non-API-key PII redaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks an agent to inspect API-key-related content, environment or configuration data, and scripts.

Mitigation: Use it only in contexts where the agent is allowed to inspect that material, and require explicit confirmation before reads involving sensitive files.

Risk: The security summary flags broad file, command, write, API-call, and logging behavior that is not tightly scoped.

Mitigation: Constrain agent permissions, review proposed commands and writes before execution, and approve API calls only after checking destination, method, and payload.

Risk: Interception or audit logs may reveal sensitive security event details if stored or shared carelessly.

Mitigation: Mask secrets in logs, limit log access and retention, and avoid exporting security logs to untrusted systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/key-guard)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include masked key status, interception logs, security findings, remediation suggestions, and proposed file, command, API, or configuration actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
