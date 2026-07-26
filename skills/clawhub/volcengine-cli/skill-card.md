## Description: <br>
Create and manage Volcengine cloud resources using the Volcengine CLI (`ve` command), including ECS, VPC, CLB, RDS, Redis, and related services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect, create, modify, and troubleshoot Volcengine infrastructure through the `ve` CLI while following account, profile, credential, and confirmation rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use cloud credentials and perform operations that create, modify, stop, delete, or register real Volcengine resources. <br>
Mitigation: Review the active account and profile before use, keep read-only operations as the default, and require explicit confirmation before write or destructive commands. <br>
Risk: The login helper can read local Volcengine CLI credential files and may automatically replace an existing login session. <br>
Mitigation: Install only where agent access to the intended Volcengine account is acceptable, and verify the current identity after authentication or re-authentication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/volc-sdk-team/skills/volcengine-cli) <br>
- [Volcengine CLI releases](https://github.com/volcengine/volcengine-cli/releases) <br>
- [Common error handling](references/common-errors.md) <br>
- [Extension APIs](references/extend-apis.md) <br>
- [ECS service notes](references/ecs.md) <br>
- [VPC service notes](references/vpc.md) <br>
- [RDS service notes](references/rds.md) <br>
- [Redis service notes](references/redis.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Volcengine CLI commands, confirmation prompts for write or destructive operations, polling guidance, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
