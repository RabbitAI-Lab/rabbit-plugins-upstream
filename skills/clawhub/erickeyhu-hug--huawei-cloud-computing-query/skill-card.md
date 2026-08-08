## Description: <br>
Helps agents query Huawei Cloud ECS, BMS, IMS, and Auto Scaling inventory, capacity, image, quota, console, password, and policy details through bundled Python SDK scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and infrastructure engineers use this skill to inspect Huawei Cloud compute resources and collect resource IDs, capacity details, images, quotas, console links, and scaling state for inventory, verification, or automation planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Huawei Cloud AK/SK credentials and can query sensitive instance access data. <br>
Mitigation: Use least-privilege credentials, prefer temporary credentials where possible, and avoid exposing credential or query output values in shared logs. <br>
Risk: Some scripts retrieve server passwords or console login URLs. <br>
Mitigation: Run password and console scripts only for explicit administrative need, restrict who can invoke them, and treat returned values as secrets. <br>
Risk: The security evidence reports disabled TLS verification. <br>
Mitigation: Use only in trusted network environments until TLS verification behavior is reviewed or corrected. <br>
Risk: The environment setup can install Python dependencies and make local setup changes. <br>
Mitigation: Run setup in an isolated virtual environment or disposable workspace and review dependency installation before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-computing-query) <br>
- [Huawei Cloud Auto Scaling Query Guide](references/as/guide.md) <br>
- [BMS Bare Metal Server Query Guide](references/bms/guide.md) <br>
- [Huawei Cloud ECS Query Guide](references/ecs/guide.md) <br>
- [IMS Image Management Service Query Guide](references/ims/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell command invocations and JSON or text query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include sensitive Huawei Cloud resource identifiers, passwords, and console URLs depending on the selected query script.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
