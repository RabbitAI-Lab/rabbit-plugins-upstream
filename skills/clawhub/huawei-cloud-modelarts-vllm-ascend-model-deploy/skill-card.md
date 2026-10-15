## Description:

Guides developers through deploying open-source language models on Huawei Cloud ModelArts with vLLM-Ascend and validating an OpenAI-compatible inference endpoint.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare model weights and container images, choose a supported Ascend deployment topology, deploy a ModelArts online service, and test inference. The source limits this workflow to functional validation and prototyping rather than production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials may be exposed or overprivileged.

Mitigation: Use least-privileged temporary Huawei Cloud credentials; do not give IAM passwords to an agent unless necessary.

Risk: Disabling TLS verification can expose credentials and deployment traffic.

Mitigation: Require normal TLS verification or a trusted enterprise CA bundle instead of verify=False or -k.

Risk: An unauthenticated Internet-accessible endpoint may expose a paid inference service.

Mitigation: Do not expose auth_type NONE endpoints publicly; limit unauthenticated use to isolated test environments.

Risk: Running an unverified optional KooCLI installer can execute untrusted code.

Mitigation: Download the installer from a trusted source and verify its integrity before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-modelarts-vllm-ascend-model-deploy)
- [vLLM-Ascend model deployment documentation](https://docs.vllm.ai/projects/ascend/zh-cn/latest/tutorials/models/)
- [Huawei Cloud ModelArts CreateInferService API](https://support.huaweicloud.com/api-modelarts/CreateInferService.html)
- [ModelArts console deployment guide](references/modelarts-console-guide.md)
- [Ascend hardware compatibility matrix](references/ascend-hardware-matrix.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands, deployment scripts, and API configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can generate deployment and health-check scripts and instructions for API or console deployment.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
