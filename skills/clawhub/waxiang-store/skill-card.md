## Description:

挖象浏览器打开店铺工作流：在挖象浏览器中登录之后，打开用户指定分组指定名称的店铺。当用户需要在挖象浏览器中打开某个店铺（给出店铺名称与所属分组）时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[randydai](https://clawhub.ai/user/randydai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to open a named store in a named group in WaXiang Browser after confirming or completing login. It guides an agent through launching the browser with remote debugging, checking login state, optionally submitting credentials, and issuing the WaXiang store-open command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow opens a powerful browser debugging interface around an authenticated WaXiang account.

Mitigation: Review before installing, run it only with a dedicated WaXiang profile that has no unrelated sessions, and close the browser after use.

Risk: The launch command permits wildcard remote origins and exposes a local debugging endpoint.

Mitigation: Prefer a release that removes wildcard remote origins and uses a random local-only port.

Risk: Logs may expose debugger URLs, ports, or session metadata from an authenticated browser session.

Mitigation: Avoid sharing logs and redact debugger URLs, ports, and session metadata before retaining or transmitting output.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow instructions with shell command examples and JSON-RPC payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires store name and store group; may use optional WaXiang credentials, browser path, local debugging port, and isolated user data directory.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
