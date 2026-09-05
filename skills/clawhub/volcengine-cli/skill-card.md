## Description:

Create and manage Volcengine cloud resources using the Volcengine CLI (`ve` command), including services such as ECS, VPC, CLB, RDS, Redis, and related troubleshooting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to inspect, create, update, and delete Volcengine infrastructure through the `ve` CLI, with service-specific notes for common Volcengine products. It also supports troubleshooting failed CLI calls, console login setup, and fallback OpenAPI calls when CLI metadata is incomplete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer path can execute remotely downloaded code and update local `ve` skills.

Mitigation: Install only from trusted Volcengine distribution paths, prefer npm or the bundled installer with a pinned version, review the installer before running it, and set `VOLCENGINE_CLI_SKIP_SKILLS=1` when automatic skill updates are not desired.

Risk: The skill can create, modify, or delete Volcengine cloud resources after confirmation.

Mitigation: Use least-privilege Volcengine credentials, verify the selected profile and region, and require explicit confirmation before write or destructive operations.

Risk: Credential and session configuration is involved in CLI login and helper-script fallback paths.

Mitigation: Avoid exposing access keys or session tokens in prompts, logs, shell history, or process arguments, and prefer scoped temporary credentials where practical.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/volc-sdk-team/skills/volcengine-cli)
- [Volcengine CLI GitHub releases](https://github.com/volcengine/volcengine-cli/releases)
- [Volcengine CLI CDN](https://cloudcache.volccdn.com/ve)
- [Console Login Procedure](references/console-login.md)
- [Common Error Handling](references/common-errors.md)
- [Cloud Control API Service Notes](references/cloudcontrol.md)
- [Extended APIs](references/extend-apis.md)
- [ECS Service Notes](references/ecs.md)
- [VPC Service Notes](references/vpc.md)
- [RDS Service Notes](references/rds.md)
- [Redis Service Notes](references/redis.md)
- [VKE Service Notes](references/vke.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, CLI arguments, JSON examples, and operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce commands that call Volcengine APIs or helper scripts and may reference environment variables for credentials, region, endpoints, profile selection, and installer behavior.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
