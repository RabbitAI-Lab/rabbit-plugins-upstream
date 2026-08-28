## Description:

使用 `baijimu` CLI 开发、冻结、审核、发布、安装、升级或卸载 Bundle，以及在 Bundle 内开发 Module、Skill、Agent 和平台应用资源。

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和平台运营人员使用该技能管理 Baijimu Bundle 的开发、冻结、审核、发布、安装、升级和卸载流程，并在 Bundle 内维护 Module、Skill、Agent 和平台应用资源。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Baijimu CLI lifecycle commands can change project, publishing, review, installation, upgrade, or uninstall state.

Mitigation: Verify the target workspace, project, Runtime, CLI version, and command help before running lifecycle commands, and stop at explicit permission or human-review blockers.

Risk: Using stale documentation, mismatched CLI parameters, or legacy independent Module workflows can produce incorrect Bundle lifecycle actions.

Mitigation: Use `baijimu capabilities --offline --json`, local `baijimu <command> --help`, and the fixed-version Bundle documentation before executing commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/momoplan/skills/baijimu-bundle-development)
- [Publisher profile](https://clawhub.ai/user/momoplan)
- [Project homepage](https://github.com/momoplan/baijimu-platform-skill)
- [Baijimu Bundle development documentation](https://docs.baijimu.com/development/bundle-development/)
- [Baijimu Bundle change and release workflow](https://docs.baijimu.com/development/bundle-development/change-and-release/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is bound to the local baijimu CLI version and the target workspace, project, Bundle, and Runtime context.]

## Skill Version(s):

1.6.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
