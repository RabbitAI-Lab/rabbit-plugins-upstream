## Description:

End-to-end functional testing framework for Huawei Cloud skills that runs a three-tier, eight-phase pipeline for installation checks, analysis, test generation, live execution, orchestration, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to test Huawei Cloud skills through staged installation checks, capability analysis, test-case generation, real-environment execution, orchestration checks, and consolidated reports. It is intended for isolated skill quality validation rather than production workload operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Huawei Cloud credentials to run live cloud commands.

Mitigation: Run it only in an isolated test environment with least-privilege, non-production credentials.

Risk: Write operations may affect live cloud resources when enabled.

Mitigation: Keep ALLOW_WRITES disabled on production accounts, inspect generated commands before execution, and verify cleanup requirements after runs.

Risk: The skill may send execution quality telemetry.

Mitigation: Set SKILL_QUALITY_DISABLE=1 unless the reporting destination is explicitly trusted.

Risk: Phase 6 multi-skill pass labels may not prove live end-to-end execution.

Mitigation: Treat those results as scenario derivation unless the evidence shows real live execution for the specific run.

## Reference(s):

- [Architecture](artifact/references/architecture.md)
- [Output Schema Specification](artifact/references/output-schema-spec.md)
- [Phase Transition Rules](artifact/references/phase-transition-rules.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Verification Method](artifact/references/verification-method.md)
- [Phase Details](artifact/references/phase-details.md)
- [Agent Protocol](artifact/references/agent-protocol.md)
- [hcloud CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with shell command summaries and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates phase summaries and timestamped test reports in a sibling test-files directory; live phases depend on Huawei Cloud credentials and write-operation gates.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
