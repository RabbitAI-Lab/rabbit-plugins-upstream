## Description:

Use when creating, editing, or reviewing WAF 3.0 custom Lua extension plugins, plugin parameters, or request validation logic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to create, edit, and review Alibaba Cloud WAF 3.0 Lua extension plugin projects, including plugin code, parameter definitions, and manual debug test records for console deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated WAF Lua logic can block real web traffic after manual console deployment.

Mitigation: Review generated Lua carefully, run console debug cases, and associate the plugin with production rules only after confirming that block conditions are narrow enough.

Risk: Secrets or sensitive values could be embedded directly in plugin code or parameters.

Mitigation: Keep secrets in KMS-backed parameters and avoid hard-coded credentials in code or comments.

Risk: Missing parameter declarations can make block conditions match too broadly.

Mitigation: Validate every referenced params value for existence and type before using it in a punish condition.

Risk: Long-running Lua logic can exceed the 2ms execution limit and fail open at runtime.

Mitigation: Avoid infinite loops and high-cost operations, and confirm behavior with console debug tests before association.

## Reference(s):

- [Alibaba Cloud WAF Extension Plugins Documentation](https://help.aliyun.com/zh/waf/web-application-firewall-3-0/user-guide/extensions)
- [Lua API Reference](references/lua-api-reference.md)
- [Extension Plugin Console Lifecycle](references/console-lifecycle.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown guidance with Lua, JSON, and shell-style file structure examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for manual review and console entry; local files are conventions and are not imported by the platform.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
