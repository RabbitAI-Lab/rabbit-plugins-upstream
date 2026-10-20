## Description:

Creates and invokes Huawei Cloud FunctionGraph functions with optional VPC settings, environment variables, and synchronous or asynchronous invocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Huawei Cloud FunctionGraph functions, configure their networking and environment, and invoke them for testing or deployment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud access keys could be exposed or used with excessive permissions.

Mitigation: Use environment variables and a least-privilege IAM user; never print access keys or use wildcard policies unless necessary.

Risk: Creating or invoking functions can persist resources, run code, and incur charges.

Mitigation: Require explicit user confirmation before creating or invoking functions; check the target account, region, and function.

Risk: Function code, environment variables, and invocation payloads may contain sensitive data sent to Huawei Cloud.

Mitigation: Review and minimize code, environment variables, and payload data before submission.

## Reference(s):

- [Huawei Cloud FunctionGraph documentation](https://support.huaweicloud.com/functiongraph/)
- [Huawei Cloud Python SDK documentation](https://github.com/huaweicloud/huaweicloud-sdk-python-v3)
- [IAM policies guide](references/iam-policies.md)
- [SDK installation guide](references/sdk-installation-guide.md)
- [Verification method](references/verification-method.md)
- [Acceptance criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON results]

**Output Format:** [Markdown guidance and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creation returns a function URN; invocation returns a result or request ID.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
