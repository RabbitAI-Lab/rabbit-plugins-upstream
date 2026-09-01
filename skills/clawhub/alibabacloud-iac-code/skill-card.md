## Description:

Helps agents handle Alibaba Cloud infrastructure work by using the packaged iac-code workflow to design, provision, change, validate, troubleshoot, and operate ROS or Terraform-based resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to generate, review, validate, troubleshoot, and operate Alibaba Cloud infrastructure workflows, including ROS and Terraform template work, resource selection, cost estimation, and stack operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infrastructure workflows can read, create, update, or delete Alibaba Cloud resources and may incur costs.

Mitigation: Review deployment plans and cost estimates before approval, and grant only the exact RAM actions required for the approved task.

Risk: Broad cloud permissions could allow changes beyond the intended workflow.

Mitigation: Avoid product-wide FullAccess policies and action wildcards; scope credentials to the target account, region, stack, or resource where supported.

Risk: The skill downloads and runs the iac-code runtime and stores prompts, workspace paths, job state, and artifacts locally under the iac-code configuration directory.

Mitigation: Install only when this runtime behavior is intended, and review local runtime artifacts and storage practices for the deployment environment.

## Reference(s):

- [RAM permissions](references/ram-policies.md)
- [Runtime manifest](https://ros-public-tools.oss-cn-beijing.aliyuncs.com/github-releases/aliyun/iac-code/skill-runtime/releases/v0.14.0/runtime-manifest.json)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-iac-code)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown or text with code blocks, JSON protocol results, and generated infrastructure artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded progress updates, permission prompts, deployment plans, cost estimates, and artifact references; user-facing results should follow the user's preferred language.]

## Skill Version(s):

0.3.0 (source: server release metadata and scripts/iac_code.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
