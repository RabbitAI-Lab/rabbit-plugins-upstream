## Description:

挖象浏览器打开店铺工作流：在挖象浏览器中登录之后，打开用户指定分组指定名称的店铺。当用户需要在挖象浏览器中打开某个店铺（给出店铺名称与所属分组）时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[randydai](https://clawhub.ai/user/randydai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to open a named store in a specified group inside WaXiang Browser. The workflow can start WaXiang Browser in local remote-debugging mode, handle login when credentials are provided, and request the browser to open the matching store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses user-provided WaXiang login credentials when the browser is not already logged in.

Mitigation: Show the user warning before execution, request credentials only at runtime, submit them only to the official WaXiang HTTPS login page, and do not log or persist them.

Risk: The skill starts WaXiang Browser with a local remote-debugging interface for automation.

Mitigation: Bind and use the debugging interface on 127.0.0.1, run only on trusted devices, and disconnect the debugging session after the task.

Risk: The workflow may close an existing WaXiang Browser process before restarting it in debugging mode.

Mitigation: Detect a running process, clearly ask for user approval before closing it, and stop immediately if the user does not consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/randydai/skills/waxiang-store)
- [WaXiang official site](https://hao.waxiang.com)
- [WaXiang user admin](https://hao.waxiang.com/account/userAdmin)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON-RPC examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs started status, reason text, and local browser debugging port details when available.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
