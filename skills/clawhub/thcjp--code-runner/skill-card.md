## Description:

A Chinese-language code execution assistant for batch task execution, concurrent job management, execution audit logs, CI/CD workflows, and development automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and CI/CD operators use this skill to drive coding, testing, review, and deployment tasks through agent-executed commands and structured batch workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic command execution can run unintended or unsafe commands.

Mitigation: Install only in a disposable or tightly controlled environment, restrict allowed workdirs and commands, and review external packages before use.

Risk: Generic auto-confirm and password prompt automation can approve actions or disclose credentials unexpectedly.

Mitigation: Disable generic auto-confirm and password prompt automation; avoid root or sudo unless absolutely necessary.

Risk: Detailed execution and audit logs may capture sensitive code, outputs, or secrets.

Mitigation: Configure audit logs to redact secrets and retain data briefly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-runner)
- [Declared homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code blocks, shell commands, JSON examples, and audit/report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable command suggestions, configuration snippets, code changes, logs, and structured reports.]

## Skill Version(s):

1.0.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
