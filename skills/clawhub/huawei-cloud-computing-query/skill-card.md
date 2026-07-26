## Description: <br>
Queries Huawei Cloud ECS, BMS, IMS, and AS resources through packaged Python SDK scripts for inventory, specification, image, quota, and status lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to query existing Huawei Cloud compute resources, available specifications, images, quotas, identifiers, and status data for inventory, verification, and automation planning. It is intended for read-only lookup workflows, although some scripts can return sensitive server passwords or console login URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud AK/SK credentials and can access account resource data. <br>
Mitigation: Use least-privilege credentials, prefer temporary credentials where available, and avoid exposing credential values in prompts, logs, or transcripts. <br>
Risk: Some query scripts can retrieve sensitive server passwords or VNC console login URLs. <br>
Mitigation: Run password and console scripts only when explicitly needed, limit who can view outputs, and keep returned secrets out of shared logs and transcripts. <br>
Risk: The setup path can install dependencies and persist a local project ID. <br>
Mitigation: Review the environment setup step before execution and clean up generated local state such as .venv or .project_id when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-computing-query) <br>
- [Huawei Cloud Auto Scaling query guide](artifact/references/as/guide.md) <br>
- [BMS bare metal server query guide](artifact/references/bms/guide.md) <br>
- [ECS query guide](artifact/references/ecs/guide.md) <br>
- [IMS query guide](artifact/references/ims/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and summarized JSON query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Huawei Cloud resource identifiers, configuration details, quotas, passwords, or console URLs depending on the script invoked.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
