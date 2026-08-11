## Description:

Creates Huawei Cloud agent skill packages through a six-phase workflow that gathers requirements, researches CLI, SDK, and API options, generates documentation and tests, validates compliance, and prepares cleanup reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold Huawei Cloud skills from confirmed requirements, research supported execution modes, create reference docs and test assets, and run validation and cleanup checks in a controlled workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling may be under-scoped for cloud testing workflows.

Mitigation: Use least-privilege temporary Huawei Cloud credentials, avoid production accounts, and configure secrets out of band before testing.

Risk: Generated test cases can lead to shell or cloud command execution.

Mitigation: Run only in a controlled workspace, review templates/test-vars.json before execution, and block arbitrary user-provided curl endpoints or bash commands unless explicitly approved.

Risk: The security verdict is suspicious.

Mitigation: Review and scan the skill before deployment, then fix any credential, command-execution, or validation issues before allowing live cloud operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-creator)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Security audit guide](references/security-audit-guide.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Related commands](references/related-commands.md)
- [Dataflow diagram](references/dataflow-diagram.md)
- [Huawei Cloud KooCLI quickstart](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON files, shell command examples, and generated skill-directory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase summary JSON, templates/test-vars.json, validation reports, and generated skill files; cloud-command execution depends on configured Huawei Cloud credentials.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
