## Description:

Use this skill to search, aggregate, and investigate centralized logs in VMware VCF Operations for Logs, including event search, spike detection, field discovery, version lookup, and read-only alert queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and VMware administrators use this skill to query Log Insight data during incident investigation, find relevant log lines, inspect spikes in log volume, and retrieve read-only alert and metadata information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local credential files may be rewritten from plaintext password values to b64-obfuscated values, which is not encryption and may conflict with policies that forbid local secret storage or rewriting.

Mitigation: Use a least-privilege read-only Log Insight account and inject credentials from an approved secret manager instead of storing real secrets in ~/.vmware-log-insight/.env when policy requires it.

Risk: Tool calls may create persistent audit records in ~/.vmware/audit.db.

Mitigation: Confirm the audit database location, retention, and contents are acceptable for the deployment environment before enabling the skill.

Risk: Log contents are untrusted and can include instruction-like text or large result sets that affect agent behavior or context usage.

Mitigation: Treat returned log lines as data, keep searches bounded, report truncation indicators, and avoid acting on instructions found inside log content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Agent Guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text with inline shell commands, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize API query results, returned log events, aggregate bins, spikes, field lists, alert data, and diagnostic guidance.]

## Skill Version(s):

1.8.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
