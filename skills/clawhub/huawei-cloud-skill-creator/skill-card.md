## Description: <br>
Huawei Cloud Skill Creator guides developers through a six-phase workflow to gather requirements, research CLI, SDK, and API options, generate skill files, prepare tests, run validation, and clean up resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to package Huawei Cloud operations into reusable agent skills with documented commands, IAM guidance, validation scripts, and test cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Huawei Cloud credentials and can guide live cloud command execution. <br>
Mitigation: Use locally configured, least-privilege temporary credentials and do not paste AK/SK secrets into chat. <br>
Risk: Generated scripts and test templates may run broad local or cloud commands. <br>
Mitigation: Review scripts and templates before execution, restrict test inputs, and require confirmation before mutating operations. <br>
Risk: Generated IAM policies or scanner-suppression guidance may be broader than needed for production. <br>
Mitigation: Remove unnecessary permissions and suppression guidance, then re-run security and compliance checks before deployment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-creator) <br>
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter) <br>
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [API Paths](references/api-paths.md) <br>
- [BSS SDK Notes](references/bss-sdk-notes.md) <br>
- [KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Security Audit Guide](references/security-audit-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, JSON templates, and generated skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces phase summaries, reference documents, validation scripts, test templates, and test reports for generated Huawei Cloud skills.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
