## Description:

This deprecated skill now only directs agents to migrate to the replacement @lihengdao/aigc-web-push skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this package as a migration notice for an older Weixin public-account push skill. It points them to the maintained @lihengdao/aigc-web-push replacement instead of continuing to rely on the deprecated package.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the linked replacement skill as already reviewed because this deprecated package is clean.

Mitigation: Review the replacement skill's permissions, configuration guidance, publisher context, and security posture before installing it or connecting accounts.

Risk: Users may continue relying on the deprecated weixin-mp-push package even though it is no longer maintained.

Mitigation: Use this package only as a migration notice and move to the maintained replacement workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/skills/weixin-mp-push)
- [Replacement ClawHub skill](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Replacement GitHub repository](https://github.com/lihengdao/AIGC-Web-Push)
- [Replacement configuration guide](https://app.pcloud.ac.cn/design/aigc-web-push.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown text with an inline installation command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is a migration notice and does not define executable agent behavior.]

## Skill Version(s):

3.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
