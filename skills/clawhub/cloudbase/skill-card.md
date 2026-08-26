## Description:

CloudBase helps agents build, deploy, debug, migrate, and troubleshoot Tencent CloudBase applications across Web/H5, WeChat Mini Programs, mobile apps, databases, cloud functions, CloudRun, storage, authentication, and AI integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, deploy, and review CloudBase-backed applications while routing work to the relevant CloudBase domain guidance for auth, data, functions, CloudRun, storage, UI, AI, operations, and specification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation rules and security-sensitive examples may lead an agent to create insecure authentication, persistence, deployment, telemetry, or public endpoint behavior.

Mitigation: Install only for intentional CloudBase work and manually verify token validation, access rules, data retention, exposed identifiers or conversations, and generated auth, permission, and public endpoint code before use.

Risk: CloudBase management tasks may involve MCP or CLI operations that change cloud resources.

Mitigation: Review proposed CloudBase operations, resolve the full EnvId explicitly, and confirm destructive or production write actions before execution.

## Reference(s):

- [CloudBase Skill Page](https://clawhub.ai/binggg/skills/cloudbase)
- [Activation Map](references/activation-map.yaml)
- [CloudBase Scenarios](references/scenarios.md)
- [Deployment Workflow](references/deployment-workflow.md)
- [MCP Setup](references/mcp-setup.md)
- [Tooling Fallback](references/tooling-fallback.md)
- [Console Entry Points](references/console-links.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase MCP or CLI operation guidance, implementation steps, deployment notes, and review findings.]

## Skill Version(s):

1.92.71 (source: server release metadata; artifact frontmatter reports 2.32.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
