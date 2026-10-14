## Description:

Query and analyze Kubernetes Pod stdout and stderr logs, CCE LogConfig-collected application logs, Huawei Cloud LTS log streams, and CCE audit logs for CCE workloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site reliability engineers use this skill to inspect CCE workload logs, discover LogConfig to LTS stream mappings, summarize audit events, and identify abnormal log patterns. It can also preview and, after explicit confirmation, create or delete CCE LogConfig collection rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reachable cloud and Kubernetes administration functions go beyond the documented logging purpose.

Mitigation: Install only in a controlled environment, replace the shared dispatcher with a skill-specific allowlist for documented log tools, and use a dedicated least-privilege Huawei Cloud identity.

Risk: LogConfig creation or deletion can change cluster log collection behavior.

Mitigation: Require preview before execution and run mutating LogConfig operations only after explicit user confirmation with confirm=true.

Risk: Log output can contain credentials, tokens, cookies, authorization headers, personal data, or sensitive workload details.

Mitigation: Use bounded time ranges and small limits, summarize repeated patterns, and redact sensitive values instead of returning full raw log payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-cce-log-analyzer)
- [workflow.md](references/workflow.md)
- [risk-rules.md](references/risk-rules.md)
- [output-schema.md](references/output-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and structured JSON-like fields for log query, audit, LogConfig, and abnormality analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should summarize patterns, counts, timestamps, affected resources, redacted examples, and bounded next steps rather than full sensitive log payloads.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
