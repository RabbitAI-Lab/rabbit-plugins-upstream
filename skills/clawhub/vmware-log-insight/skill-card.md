## Description:

Searches, aggregates, and investigates centralized VMware VCF Operations for Logs data from ESXi hosts, vCenter, and VMs, including full-text log search, spike detection, field discovery, and read-only alert queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and VMware operators use this skill to inspect centralized VMware log lines, find error windows, detect log-volume spikes, and gather read-only alert context during incident investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs the external vmware-log-insight package.

Mitigation: Install only from a trusted package source and verify the package source before deployment.

Risk: The skill handles local VMware Log Insight credentials.

Mitigation: Use a dedicated read-only Log Insight account, keep ~/.vmware-log-insight/.env out of backups and sync tools, and prefer injecting passwords from a secret manager.

Risk: Log text can contain untrusted or instruction-shaped content.

Mitigation: Treat returned log lines as data, keep searches bounded, and rely on the skill's sanitization and truncation behavior when presenting results.

## Reference(s):

- [vmware-log-insight ClawHub page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured log-query guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only log search results, aggregation summaries, spike timestamps, field lists, alert context, and troubleshooting guidance.]

## Skill Version(s):

1.8.16 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
