## Description:

End-to-end functional testing framework for Huawei Cloud skills with a three-tier pipeline for single-skill unit testing, multi-skill orchestration checks, live flow testing, structured JSON outputs, cleanup tracking, and consolidated reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to test Huawei Cloud skills across installation, feature extraction, CLI/SDK/API feasibility research, generated test cases, live execution, orchestration checks, full-flow scenarios, and final reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run generated local commands and live Huawei Cloud operations under user credentials.

Mitigation: Install only in an isolated test environment with scoped Huawei Cloud credentials and a dedicated test project.

Risk: Write operations can affect cloud resources when explicitly enabled.

Mitigation: Keep ALLOW_WRITES unset unless the exact generated actions have been reviewed and the test project can tolerate those changes.

Risk: Multi-skill Phase 6 pass results may reflect derived scenarios rather than proof of live execution.

Mitigation: Do not treat multi-skill Phase 6 pass results as proof of live execution; verify whether live API calls actually ran.

Risk: Sibling auto-discovery can expand a test run beyond the intended single skill.

Mitigation: Use --no-siblings or SIBLING_LIMIT=0 when testing one skill.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [Architecture](references/architecture.md)
- [hcloud CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Output Schema Specification](references/output-schema-spec.md)
- [Phase Transition Rules](references/phase-transition-rules.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase summary JSON and consolidated reports; live phases require Huawei Cloud credentials and write-operation gates.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
