## Description:

Huawei Cloud CCI (Cloud Container Instance) full lifecycle management using hcloud CLI for Namespace, Network, Deployment, StatefulSet, Pod, EIPPool, logs, metrics, and status workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud CCI serverless container resources through hcloud CLI workflows, including creation, status inspection, logs, scaling, updates, and cleanup. It is intended for command-line CCI administration where destructive operations require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script includes unsafe shell execution while auto-detecting the Huawei Cloud project ID.

Mitigation: Replace shell=True with an argument list, validate the region value before invocation, and review the helper before installation or use.

Risk: The skill can guide broad or destructive cloud actions, including namespace deletion, network deletion, public IP allocation, Secret and RBAC operations, and bulk cleanup.

Mitigation: Use least-privilege Huawei credentials scoped to the intended project and region, preview commands and resource scope first, and require explicit confirmation for every delete or bulk cleanup path.

Risk: Cloud credentials could be exposed if users paste AK/SK values or commands echo secrets.

Mitigation: Check only credential presence, prefer configured profiles or environment variables, and do not display AK/SK values in conversation, commands, logs, or output.

Risk: Incorrect CCI parameters can fail deployments or create resources in an unintended state.

Mitigation: Run hcloud CCI operation help before command construction and verify required namespace, network, region, VPC, subnet, security group, resource request, and limit parameters.

## Reference(s):

- [Huawei Cloud CCI Container Instance Lifecycle Management](artifact/SKILL.md)
- [CCI Common Workflows](artifact/references/common-workflows.md)
- [CCI Operation Catalog](artifact/references/cci-operation-catalog.md)
- [CCI Parameter Format Rules](artifact/references/parameter-format.md)
- [Network Lifecycle Management](artifact/references/task-network-management.md)
- [IAM Permission Policies for CCI Operations](artifact/references/iam-policies.md)
- [Troubleshooting Guide for CCI hcloud CLI Issues](artifact/references/troubleshooting.md)
- [Step-by-Step Verification Process for CCI Skill Functionality](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, checklists, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include destructive cloud administration commands only after preview, risk warning, and explicit user confirmation.]

## Skill Version(s):

0.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
