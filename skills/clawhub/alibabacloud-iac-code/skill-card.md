## Description:

Routes Alibaba Cloud infrastructure requests through the packaged iac-code bridge to design, provision, change, deploy, review, validate, troubleshoot, and manage ROS or Terraform resources and runtime caches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to delegate Alibaba Cloud infrastructure workflows to the packaged iac-code runtime, including template work, resource selection, cost estimation, ROS stack operations, and cache inspection or cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a downloaded local runtime with broad inherited environment access.

Mitigation: Install only when the runtime publisher is trusted, use a dedicated shell or session without unrelated API keys, and review scan findings before use.

Risk: Infrastructure workflows can read or change Alibaba Cloud resources.

Mitigation: Use narrowly scoped RAM permissions and review every permission request or deployment confirmation before allowing changes.

Risk: Generated templates, plans, or cost estimates may be incomplete or incorrect for the target environment.

Mitigation: Review generated IaC, validate or preview templates, and confirm costs and deployment parameters before applying them.

## Reference(s):

- [RAM permissions](references/ram-policies.md)
- [Skill manifest](references/manifest.json)
- [iac-code runtime manifest](https://ros-public-tools.oss-cn-beijing.aliyuncs.com/github-releases/aliyun/iac-code/skill-runtime/releases/v0.15.0/runtime-manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text responses with generated infrastructure templates, commands, plans, permission prompts, and cache-maintenance results when applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated ROS or Terraform content, deployment plans, cost information, runtime-cache results, and bounded JSON bridge results.]

## Skill Version(s):

0.4.0 (source: release metadata, references/manifest.json, script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
