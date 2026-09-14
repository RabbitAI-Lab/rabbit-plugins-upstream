## Description:

Helps agents develop, design, build, deploy, debug, migrate, and troubleshoot CloudBase projects across Web, WeChat Mini Program, mobile, authentication, databases, cloud functions, CloudRun, storage, AI model, AI agent, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide CloudBase application work from scenario routing through implementation, resource setup, deployment, and code review. It is intended for CloudBase-backed projects, not non-CloudBase frontends or self-hosted backends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill can make persistent plugin or MCP tooling changes.

Mitigation: Review the requested tooling changes before installation, pin or verify package versions where possible, and limit installation to the intended agent or IDE target.

Risk: The security evidence flags hidden AI deployment directions with unsafe cleanup patterns.

Mitigation: Treat hidden deployment directions as documentation for human review and do not run cleanup or deployment commands automatically.

Risk: The security evidence warns against reusing JWT multi-tenant examples without proper token verification.

Mitigation: Require explicit token verification and application-specific authorization checks before adapting JWT multi-tenant examples.

## Reference(s):

- [CloudBase Development Guidelines](artifact/SKILL.md)
- [Activation Map](artifact/references/activation-map.yaml)
- [MCP Setup](artifact/references/mcp-setup.md)
- [Tooling Fallback](artifact/references/tooling-fallback.md)
- [Deployment Workflow](artifact/references/deployment-workflow.md)
- [CloudBase CLI](artifact/references/cloudbase-cli/SKILL.md)
- [Web Development](artifact/references/web-development/SKILL.md)
- [Cloud Functions](artifact/references/cloud-functions/SKILL.md)
- [CloudBase Code Review](artifact/references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to read scenario-specific local reference files before acting.]

## Skill Version(s):

1.92.99 (source: ClawHub release metadata; artifact frontmatter reports 2.34.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
