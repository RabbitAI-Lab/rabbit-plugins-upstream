## Description:

Searches, aggregates, and investigates centralized VMware VCF Operations for Logs data through read-only log search, field discovery, spike detection, alert queries, and CLI/MCP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and VMware operations teams use this skill to inspect actual log lines, query read-only alert data, find log-volume spikes, and gather evidence for incident investigation in VMware/vSphere/ESXi environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the externally installed vmware-log-insight package.

Mitigation: Install only if the pinned package and linked source are trusted for the target environment.

Risk: Local configuration, .env files, audit databases, and retrieved logs can contain sensitive operational data or credentials.

Mitigation: Use a dedicated read-only Log Insight service account, protect local .env and audit database files, and prefer secret-manager or process-level environment injection over stored passwords.

Risk: Disabling TLS verification can expose Log Insight sessions outside controlled lab conditions.

Mitigation: Keep TLS verification enabled except for controlled lab appliances.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON snippets when tool or CLI output is discussed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only operational guidance and interpretations of Log Insight query results; it does not create, edit, ingest, or delete Log Insight data.]

## Skill Version(s):

1.8.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
