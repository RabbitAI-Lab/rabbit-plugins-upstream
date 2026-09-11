## Description:

挖象浏览器打开店铺工作流：在挖象浏览器中登录之后，打开用户指定分组指定名称的店铺。当用户需要在挖象浏览器中打开某个店铺（给出店铺名称与所属分组）时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[randydai](https://clawhub.ai/user/randydai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to open a named shop in a specified WaXiang browser group after confirming login and browser launch requirements. It is intended for local, user-authorized shop startup workflows on a trusted machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow opens an authenticated local browser debugging interface.

Mitigation: Use only on a trusted machine, bind the debugging interface to 127.0.0.1, choose an unpredictable free port, and use a dedicated WaXiang browser profile.

Risk: Wildcard Origin allowance and full CDP response logging may expose unnecessary debugging or session details.

Mitigation: Remove the wildcard Origin allowance unless required by the local client, and avoid logging complete CDP responses when they may contain sensitive details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/randydai/skills/waxiang-store)
- [Publisher profile](https://clawhub.ai/user/randydai)
- [WaXiang service](https://hao.waxiang.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API Calls, JSON]

**Output Format:** [Markdown workflow instructions with command snippets and JSON-RPC examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs a started status, reason text, and local browser debugging port details when available.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
