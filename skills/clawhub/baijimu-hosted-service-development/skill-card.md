## Description:

使用 `baijimu` CLI 开发和部署普通 Hosted Service 后端，覆盖 Project/Git、Rust BuildJob、Artifact、数据库迁移、Environment、Slot、Deployment、Endpoint、配置和服务鉴权。

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide Baijimu Hosted Service backend delivery, including builds, artifact selection, environment setup, deployments, endpoints, authentication, configuration, and database migrations. It is scoped to ordinary hosted backend application delivery, not Bundle/Module lifecycles, platform-service release, or infrastructure changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production deployments and database migrations can change live service state.

Mitigation: Review proposed baijimu commands before execution and verify workspace, Project, Environment, Deployment, Endpoint, and Artifact identifiers before production changes.

Risk: Failed database migrations may not automatically roll back committed database changes.

Mitigation: Use expand/contract and forward-recovery migration practices, then verify Migration Operation and Attempt status before treating a deployment as complete.

Risk: CLI or documentation version mismatches can lead to unsupported parameters or incorrect workflow assumptions.

Mitigation: Check `baijimu capabilities --offline --json`, relevant `--help` output, and fixed-version documentation; stop and report a version mismatch when the required parameters are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/momoplan/skills/baijimu-hosted-service-development)
- [Baijimu platform skill homepage](https://github.com/momoplan/baijimu-platform-skill)
- [Baijimu backend development documentation](https://docs.baijimu.com/development/backend-development/)
- [Baijimu database migrations documentation](https://docs.baijimu.com/development/backend-development/database-migrations/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires terminal access and the baijimu CLI.]

## Skill Version(s):

1.6.1 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
