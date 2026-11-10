## Description:

Guides users through deploying open source large language models on Huawei Cloud ModelArts inference with vLLM-Ascend and Ascend NPUs.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare models, images, deployment scripts, and ModelArts online services for vLLM-Ascend inference, then verify the OpenAI-compatible endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports credential and network weaknesses, unverified installation steps, host configuration changes, and partial inspection coverage.

Mitigation: Before considering use, have a qualified reviewer inspect the affected code and bundled wheel, verify installer and image provenance, and address the reported TLS, public HTTP, and host configuration concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-modelarts-vllm-ascend-model-deploy)
- [Huawei Cloud ModelArts deployment best practice](https://support.huaweicloud.com/intl/zh-cn/bestpractice-modelarts/modelarts_10_3121.html)
- [CreateInferService API](https://support.huaweicloud.com/api-modelarts/CreateInferService.html)
- [ModelArts inference migration guide](https://support.huaweicloud.com/intl/zh-cn/inference-modelarts/inference2.0-modelarts-0080.html)
- [ModelArts inference guide](https://support.huaweicloud.com/intl/zh-cn/inference-modelarts/inference2.0-modelarts-0002.html)
- [Deployment form decision guide](artifact/references/deployment-form-decision.md)
- [ModelArts console deployment guide](artifact/references/modelarts-console-guide.md)
- [Artifact validation checklist](artifact/references/artifact-check.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown guidance with Python and shell scripts, command examples, and deployment configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated deployment and health-check scripts, API request examples, and endpoint verification steps.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
