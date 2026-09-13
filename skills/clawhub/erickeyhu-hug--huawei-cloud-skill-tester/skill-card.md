## Description: <br>
End-to-end functional testing framework for Huawei Cloud skills, covering single-skill unit testing, multi-skill orchestration, end-to-end full-flow testing, structured JSON outputs, and consolidated reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to test Huawei Cloud skills through phased installation checks, feature extraction, technical research, test generation, real-environment execution, orchestration checks, lifecycle verification, cleanup tracking, and final reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated commands and cloud write operations may run with Huawei Cloud credentials without the user confirmations described by the skill. <br>
Mitigation: Use disposable, least-privilege Huawei Cloud test credentials in an isolated environment, and inspect generated Phase 3 test cases before Phase 4 execution. <br>
Risk: Real-environment lifecycle and orchestration tests can create, modify, or delete cloud resources. <br>
Mitigation: Avoid production accounts, confirm every mutating test step, and review cleanup records and manual cleanup instructions after execution. <br>
Risk: Broad run modes such as --all-installed and reset modes such as --fresh can affect local skill installs, phase files, reports, and test state. <br>
Mitigation: Run against an explicit skill list whenever possible and use --all-installed or --fresh only after confirming the affected local files and resources are acceptable to change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-skill-tester) <br>
- [KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Architecture](references/architecture.md) <br>
- [KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Output Schema Specification](references/output-schema-spec.md) <br>
- [Phase Transition Rules](references/phase-transition-rules.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON files] <br>
**Output Format:** [Markdown guidance with shell commands, generated code snippets, and structured JSON phase reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces chained phase summaries, cleanup records, and consolidated JSON/Markdown reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
