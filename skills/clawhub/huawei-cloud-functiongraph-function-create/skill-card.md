## Description:

Create FunctionGraph functions on Huawei Cloud for cloud function deployment, uploads, and serverless workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to create Huawei Cloud FunctionGraph functions from supplied names, runtimes, handlers, and code content. It supports quick function creation, batch creation, deployment workflow foundations, and CI/CD integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad Huawei Cloud permissions can expose or mutate cloud resources beyond the intended FunctionGraph deployment scope.

Mitigation: Use a dedicated IAM user, avoid full-access policy examples, and scope permissions to the target project and functions.

Risk: Function creation, trigger creation, test triggers, or debug settings can leave mutable cloud resources active after verification.

Mitigation: Review resource and trigger changes before running them, then remove test triggers or debug settings after verification.

## Reference(s):

- [FunctionGraph Documentation](https://support.huaweicloud.com/functiongraph/)
- [Huawei Cloud FunctionGraph Product Documentation](https://support.huaweicloud.com/productdesc-functiongraph/index.html)
- [Huawei Cloud Python SDK](https://github.com/huaweicloud/huaweicloud-sdk-python-v3)
- [IAM Policies](references/iam-policies.md)
- [SDK Installation Guide](references/sdk-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, Python code, configuration examples, and structured JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or verify Huawei Cloud FunctionGraph resources when run with valid credentials and permissions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
