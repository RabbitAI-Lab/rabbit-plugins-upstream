## Description:

Guides users through deploying open source large language models as online inference services on Huawei Cloud ModelArts with vLLM-Ascend and Ascend NPUs.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare model weights, container images, and deployment scripts, then deploy and verify vLLM-Ascend inference services on Huawei Cloud ModelArts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports weakened connection security and an unverified installer in the deployment workflow.

Mitigation: Use official HTTPS sources, verify downloaded installers and images against trusted checksums or signatures, and review commands before execution.

Risk: Deployment may expose inference services or make host-level networking changes.

Mitigation: Restrict endpoints to trusted networks, require authentication, and review host and network changes before applying them.

Risk: Deployment uses cloud credentials to upload assets and create services.

Mitigation: Use least-privilege credentials, pass tokens through environment variables or protected token files, and keep credentials out of commands and logs.

## Reference(s):

- [Deployment form decision guide](artifact/references/deployment-form-decision.md)
- [ModelArts console deployment guide](artifact/references/modelarts-console-guide.md)
- [ModelArts API deployment guide](artifact/references/api-deployment-guide.md)
- [IAM policies and credential permissions](artifact/references/iam-policies.md)
- [Deployment verification guide](artifact/references/verification-method.md)
- [vLLM-Ascend model deployment documentation](https://docs.vllm.ai/projects/ascend/zh-cn/latest/tutorials/models/)
- [Huawei Cloud ModelArts deployment best practice](https://support.huaweicloud.com/intl/zh-cn/bestpractice-modelarts/modelarts_10_3121.html)
- [CreateInferService API reference](https://support.huaweicloud.com/api-modelarts/CreateInferService.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown guidance with shell commands, Python scripts, and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes single-node, multi-node, and prefill/decode deployment variants.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
