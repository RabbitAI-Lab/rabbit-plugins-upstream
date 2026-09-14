## Description:

End-to-end functional testing framework for Huawei Cloud skills, with a three-tier pipeline for single-skill unit testing, multi-skill orchestration, and end-to-end full-flow testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to validate Huawei Cloud skills through installation checks, feature analysis, technical feasibility research, generated test cases, live execution, orchestration scenarios, and consolidated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute untrusted test content with live Huawei Cloud credentials.

Mitigation: Install and run it only in an isolated test environment with disposable credentials and no production cloud access.

Risk: The skill can automatically report local session metadata during quality reporting.

Mitigation: Disable telemetry unless the data flow is explicitly accepted.

Risk: Phase 4 write tests may mutate live resources despite documented safety gates.

Mitigation: Use disposable projects and resources, review write cases before execution, and avoid granting production permissions.

## Reference(s):

- [Huawei Cloud Skill Tester on ClawHub](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-tester)
- [architecture.md](references/architecture.md)
- [output-schema-spec.md](references/output-schema-spec.md)
- [phase-transition-rules.md](references/phase-transition-rules.md)
- [acceptance-criteria.md](references/acceptance-criteria.md)
- [verification-method.md](references/verification-method.md)
- [phase-details.md](references/phase-details.md)
- [agent-protocol.md](references/agent-protocol.md)
- [cli-installation-guide.md](references/cli-installation-guide.md)
- [iam-policies.md](references/iam-policies.md)
- [Huawei Cloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and structured JSON/Markdown test artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase summary JSON files and timestamped test reports for the skills under test.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
