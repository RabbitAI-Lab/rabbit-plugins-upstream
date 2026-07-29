## Description: <br>
Huawei Cloud SWR Image Management helps agents manage Huawei Cloud Software Repository for Container namespaces, repositories, image tags, login credentials, and quotas through the hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and DevOps teams use this skill to operate Huawei Cloud SWR container image resources, including namespaces, repositories, tags, login credentials, and quota checks. It is most useful when an agent needs to propose or run hcloud CLI workflows with parameter checks, confirmation for writes, and formatted results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide destructive namespace, repository, or tag deletions in Huawei Cloud SWR. <br>
Mitigation: Require explicit user confirmation, show the exact target resources, and perform inventory checks before deletion. <br>
Risk: The skill handles cloud access keys, security tokens, and Docker login credentials, including long-lived credential flows. <br>
Mitigation: Prefer temporary credentials, least-privilege IAM policies, MFA for sensitive operations, and avoid exposing or echoing secret values. <br>
Risk: Installation guidance may involve downloading and running hcloud CLI artifacts. <br>
Mitigation: Verify hcloud downloads before running or installing them and use trusted Huawei Cloud documentation links. <br>
Risk: Broad activation could apply the skill outside intended Huawei Cloud SWR workflows. <br>
Mitigation: Narrow use to SWR and Huawei-specific image management requests before proposing commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-image-management) <br>
- [SWR API Reference Guide](references/swr-api-guide.md) <br>
- [IAM Permission Policies - SWR Image Management Skill](references/iam-policies.md) <br>
- [Huawei Cloud KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [SWR Parameter Reference](references/parameter-reference.md) <br>
- [SWR Output Format Reference](references/output-format.md) <br>
- [Verification Method - SWR Image Management Skill](references/verification-method.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and tabular summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include hcloud CLI commands, IAM policy snippets, confirmation prompts, and post-operation verification steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
