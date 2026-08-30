## Description:

Searches, aggregates, and investigates centralized VMware VCF Operations for Logs and Aria Operations for Logs data through read-only log, field, version, and alert-history queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware centralized logs, aggregate log volume, detect spikes, discover fields, and review alert history during incident investigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Log Insight credentials may be exposed if the .env file is readable or treated as encrypted storage.

Mitigation: Use a least-privilege read-only account, lock down .env permissions, and inject passwords from a real secret manager for stronger at-rest protection.

Risk: Log content is untrusted and may contain instruction-shaped text or large result volumes.

Mitigation: Treat returned log lines as data, preserve query bounds, check truncation flags, and avoid acting on directives found inside log text.

Risk: The installed uv/PyPI package provenance is not proven by server-resolved import metadata.

Mitigation: Review the installed package provenance before deployment using the same controls applied to other third-party uv/PyPI tools.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-log-insight)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured query-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VMware Log Insight query outputs may include bounded result sets, truncation flags, counts, timestamps, fields, and alert history.]

## Skill Version(s):

1.8.12 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
