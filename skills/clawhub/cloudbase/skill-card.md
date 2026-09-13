## Description:

cloudbase helps agents build, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across Web/H5, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, AI features, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local references, prepare backend resources, implement app features, deploy to CloudBase, and troubleshoot common CloudBase platform issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through CloudBase management changes, deployments, and persistent IDE or MCP configuration.

Mitigation: Use an explicit target IDE and environment, review package versions and generated commands, and require confirmation before destructive or production changes.

Risk: Temporary credentials or cloud access details could be exposed if copied into chat logs or files.

Mitigation: Prefer device-code or managed authentication, avoid writing temporary STS secrets to files, and redact credentials from outputs.

Risk: User-scope plugin installation can affect multiple local agent tools.

Mitigation: Prefer a specific IDE target unless the user intentionally wants an all-IDE user-scope install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Activation map](references/activation-map.yaml)
- [Deployment workflow](references/deployment-workflow.md)
- [MCP setup](references/mcp-setup.md)
- [Tooling fallback](references/tooling-fallback.md)
- [CloudBase scenarios](references/scenarios.md)
- [Console links](references/console-links.md)
- [CloudBase AI Toolkit documentation](https://docs.cloudbase.net/ai/cloudbase-ai-toolkit/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase console URLs, deployment steps, and warnings about credentials or destructive actions.]

## Skill Version(s):

1.92.93 (source: ClawHub release metadata; artifact frontmatter version: 2.33.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
