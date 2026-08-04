## Description: <br>
Huawei Cloud SWR image lifecycle management skill using hcloud CLI for namespaces, repositories, image tags, docker login credentials, and quota checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform operators use this skill to manage Huawei Cloud SWR container image resources through hcloud CLI commands, including namespace, repository, tag, authentication, and quota workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute destructive SWR operations, including deleting namespaces, repositories, and image tags. <br>
Mitigation: Require explicit user confirmation for every create, update, and delete operation, and show the exact hcloud command and target resource before execution. <br>
Risk: The skill handles durable registry credentials and docker login material. <br>
Mitigation: Use least-privilege IAM, prefer temporary authorization tokens, avoid printing secrets or passing passwords on command lines, and rotate long-term CreateSecret credentials. <br>
Risk: Overbroad cloud credentials could grant the agent wider SWR management authority than the task requires. <br>
Mitigation: Grant only the documented SWR permissions needed for the requested workflow and pause on permission failures until the user confirms the intended IAM policy. <br>


## Reference(s): <br>
- [SWR API Reference Guide](references/swr-api-guide.md) <br>
- [SWR Parameter Reference](references/parameter-reference.md) <br>
- [SWR Output Format Reference](references/output-format.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Task: Namespace Management](references/task-namespace-management.md) <br>
- [Task: Repository Management](references/task-repository-management.md) <br>
- [Task: Tag Management](references/task-tag-management.md) <br>
- [Task: Auth Management](references/task-auth-management.md) <br>
- [Task: Quota Management](references/task-quota-management.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI Release Notes](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [Huawei Cloud SWR Console](https://console.huawei.com/swr) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown with inline hcloud and docker command examples plus structured command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read operations may produce formatted tables or JSON-derived summaries; write and delete operations require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
