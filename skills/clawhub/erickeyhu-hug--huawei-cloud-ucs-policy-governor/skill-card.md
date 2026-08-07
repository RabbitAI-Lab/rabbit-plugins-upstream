## Description: <br>
Huawei Cloud UCS Policy Governor helps agents manage UCS policy instances, policy definitions, enforcement state, enforcement jobs, and fleet compliance using the hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and cloud administrators use this skill to administer Huawei Cloud UCS policy governance, including policy instance lifecycle, enforcement enablement, job-status checks, and fleet compliance review. <br>

### Deployment Geography for Use: <br>
Global, subject to Huawei Cloud regional availability and local access controls. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide policy creation, update, deletion, and enforcement-state changes in Huawei Cloud UCS. <br>
Mitigation: Install it only for UCS policy administration, use least-privilege or temporary credentials, and run mutation commands only against explicitly approved test or production resources. <br>
Risk: Audit and verification workflows may involve cluster credentials or generated kubeconfig material. <br>
Mitigation: Treat kubeconfig and Huawei Cloud AK/SK/SecurityToken values as sensitive credentials; protect them during use and remove temporary material after use. <br>
Risk: Incorrect policy scope, template IDs, or enforcement actions can cause failed governance rollout or unexpected enforcement behavior. <br>
Mitigation: List and verify policy definitions before creation, start with warning or staging rollout where appropriate, and confirm target cluster or fleet group scope before applying changes. <br>


## Reference(s): <br>
- [UCS Policy API Reference Guide](references/ucs-policy-api-guide.md) <br>
- [IAM Permission Policies - UCS Policy Governor Skill](references/iam-policies.md) <br>
- [Verification Method - UCS Policy Governor Skill](references/verification-method.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Task: Policy Management](references/task-policy-management.md) <br>
- [Task: Compliance Audit](references/task-compliance-audit.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline hcloud CLI commands and JSON policy examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include read-only audit commands and state-changing policy management commands; user approval and least-privilege credentials are expected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
