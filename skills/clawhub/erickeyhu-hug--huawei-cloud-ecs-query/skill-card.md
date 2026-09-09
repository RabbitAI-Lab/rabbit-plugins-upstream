## Description: <br>
Queries Huawei Cloud ECS resources in read-only mode, including instances, flavors, keypairs, quotas, server groups, block devices, NICs, VNC console URLs, launch templates, recycle bin, scheduled events, and tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud ECS inventory, capacity, quotas, tags, network attachments, and server details without creating, modifying, or deleting cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud credentials can read ECS inventory and may expose ECS passwords or console login URLs. <br>
Mitigation: Use tightly scoped or temporary credentials, avoid password and console permissions unless needed, and treat returned passwords or console URLs as secrets. <br>
Risk: Disabled TLS verification can weaken transport validation. <br>
Mitigation: Do not run the skill on networks where disabled TLS verification is unacceptable; review the HTTP configuration before deployment. <br>
Risk: Environment setup installs Python dependencies before running queries. <br>
Mitigation: Run setup in a controlled environment and review the listed Huawei Cloud SDK dependencies before installation. <br>


## Reference(s): <br>
- [Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ecs-query) <br>
- [Query Guide](references/guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON query results from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query results depend on Huawei Cloud credentials, region, project, permissions, and selected ECS script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
