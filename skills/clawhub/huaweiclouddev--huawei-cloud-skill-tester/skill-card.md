## Description:

End-to-end functional testing framework for Huawei Cloud skills with a three-tier pipeline for single-skill testing, multi-skill orchestration, real-environment execution, cleanup checks, and consolidated reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and cloud skill maintainers use this skill to validate Huawei Cloud agent skills through staged installation checks, capability analysis, test-case generation, live execution, orchestration checks, and final reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute generated shell/Python test content and live Huawei Cloud actions with discovered credentials.

Mitigation: Install it only in an isolated test workspace with non-production credentials, least-privilege IAM, a constrained region/project, and expected billing and cleanup checks.

Risk: Write-operation safety claims may not fully match implementation behavior.

Mitigation: Review generated Phase 3 test cases before execution and disable or patch the Phase 4 write execution path unless explicit approval is enforced.

Risk: Running against arbitrary third-party skills or production accounts can create cloud resource, billing, or cleanup exposure.

Mitigation: Use dedicated test accounts and review resource cleanup results before reruns or broader deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-tester)
- [architecture.md](references/architecture.md)
- [output-schema-spec.md](references/output-schema-spec.md)
- [phase-details.md](references/phase-details.md)
- [phase-transition-rules.md](references/phase-transition-rules.md)
- [acceptance-criteria.md](references/acceptance-criteria.md)
- [verification-method.md](references/verification-method.md)
- [agent-protocol.md](references/agent-protocol.md)
- [Huawei Cloud CLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON and Markdown test report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase summary JSON files and final JSON/Markdown reports in sibling test artifact directories.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
