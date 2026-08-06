## Description: <br>
End-to-end functional testing framework for Huawei Cloud skills, covering single-skill unit testing, multi-skill orchestration, end-to-end full-flow testing, structured JSON phase outputs, and chain verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to validate Huawei Cloud skills through installation checks, feature extraction, CLI/SDK/API feasibility research, test generation, real-environment execution, orchestration testing, cleanup, and consolidated reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run generated shell or Python commands and perform Huawei Cloud write operations with credentials. <br>
Mitigation: Run it only in an isolated test account with least-privilege temporary Huawei Cloud credentials; do not use production AK/SK or valuable billing resources. <br>
Risk: Generated phase files or execution plans could trigger cloud changes before the operator has fully reviewed them. <br>
Mitigation: Inspect generated phase files before phase 4 or phase 6 and require explicit review before executing mutating tests. <br>


## Reference(s): <br>
- [Huawei Cloud Skill Tester](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-tester) <br>
- [Huawei Cloud CLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Architecture](references/architecture.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Output Schema Specification](references/output-schema-spec.md) <br>
- [Phase Transition Rules](references/phase-transition-rules.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, markdown] <br>
**Output Format:** [Markdown guidance with shell commands, JSON phase reports, generated test cases, and consolidated reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces structured phase summaries and final reports for Huawei Cloud skill test workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
