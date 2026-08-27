## Description:

Alibaba Cloud Simple Log Service (SLS) ingestion management for an already-deployed LoongCollector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to turn natural-language LoongCollector and Alibaba Cloud SLS collection-operations requests into verifiable CLI workflows for onboarding, configuration management, machine-group management, SLS Lens queries, and basic troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and, after approval, modify Alibaba Cloud SLS resources using the user's existing CLI profile.

Mitigation: Review every normalized diff before approving writes, run dry-runs before actual writes, and keep RAM permissions scoped to the target project and logstore.

Risk: Credential or local profile details could be exposed if an agent reads or prints credential files.

Mitigation: Use the bundled preflight and CLI profile checks without reading credential file contents, and configure credentials outside the agent session.

Risk: Optional raw HTTPS fallback can capture unmasked HTTP request or response bodies.

Mitigation: Leave RawHttpsFallback disabled unless there is an explicit data-governance reason and the user intentionally enables it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-loongcollector-ops)
- [Capability router](artifact/references/navigation.md)
- [Prerequisites](artifact/references/prerequisites.md)
- [Risk and approval](artifact/references/risk-and-approval.md)
- [RAM policies](artifact/references/ram-policies.md)
- [Pipeline configuration](artifact/references/pipeline-config.md)
- [AgentSight input](artifact/references/input-agentsight.md)
- [AgentSight and Agentloop](artifact/references/agentsight-agentloop.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Knowledge sources](artifact/references/knowledge-sources.md)
- [Alibaba Cloud AgentSight log collection documentation](https://help.aliyun.com/zh/sls/collect-ai-agent-observability-agentsight-logs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON or YAML configuration examples, and operational status tags.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are gated by user confirmation for write operations and are expected to include evidence, normalized diffs, verification results, and rollback notes where applicable.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
