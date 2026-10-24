## Description:

Guides developers through preparing models and images, selecting an Ascend deployment layout, deploying a vLLM-Ascend online service on Huawei Cloud ModelArts, and verifying inference.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prototype Ascend NPU inference services on ModelArts, from model and container preparation through deployment and API verification. The source limits this workflow to functional validation and prototyping, not production use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified TLS connections can expose IAM credentials and deployment inputs.

Mitigation: Review before installing; use a trusted CA bundle or verified proxy CA, and do not provide IAM passwords or high-privilege access keys until TLS verification is restored.

Risk: Unaudited remote installation scripts can execute untrusted code.

Mitigation: Avoid curl-and-bash installers without integrity checks; inspect and verify downloads first.

Risk: Bearer tokens and prompts sent to exposed inference endpoints may be intercepted.

Mitigation: Use private or TLS-protected inference endpoints for authenticated requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-modelarts-vllm-ascend-model-deploy)
- [Huawei Cloud ModelArts vLLM-Ascend deployment guide](https://support.huaweicloud.com/intl/zh-cn/bestpractice-modelarts/modelarts_10_3121.html)
- [Huawei Cloud CreateInferService API](https://support.huaweicloud.com/api-modelarts/CreateInferService.html)
- [vLLM-Ascend model guides](https://docs.vllm.ai/projects/ascend/zh-cn/latest/tutorials/models/)
- [Deployment form decision guide](references/deployment-form-decision.md)
- [Artifact validation guide](references/artifact-check.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment plans and inference verification steps tailored to the selected model and deployment form.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
