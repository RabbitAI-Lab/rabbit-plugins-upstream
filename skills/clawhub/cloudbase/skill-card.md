## Description:

Use this skill when you develop, design, build, deploy, debug, migrate, or troubleshoot CloudBase projects across Web, WeChat Mini Programs, mobile apps, authentication, databases, cloud functions, CloudRun, storage, built-in AI, AI agents, operations, and specification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local reference guidance, prepare CloudBase resources, implement application features, deploy projects, and troubleshoot account, database, AI, and runtime issues.

### Deployment Geography for Use:

Global, with separate domestic China and international CloudBase account systems and endpoints.

## Known Risks and Mitigations:

Risk: The skill can guide agents through account-level CloudBase deployment and management tasks.

Mitigation: Require explicit user confirmation before any delete, destroy, force, bypass, or similarly high-impact operation.

Risk: Some examples include unsafe high-impact behavior or unsigned-JWT persistence patterns.

Mitigation: Review examples before reuse and do not copy unsigned-JWT persistence examples into production systems.

Risk: Deployment scripts and command sequences may affect live CloudBase resources.

Mitigation: Treat scripts and commands as reviewable guidance, verify the target environment explicitly, and run them only after inspection.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase MCP Setup](references/mcp-setup.md)
- [CloudBase Site Onboarding](references/site-onboarding.md)
- [CloudBase Tooling Fallback](references/tooling-fallback.md)
- [CloudBase Deployment Workflow](references/deployment-workflow.md)
- [CloudBase Activation Map](references/activation-map.yaml)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration snippets, and implementation recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CloudBase management and deployment steps that should be reviewed before execution.]

## Skill Version(s):

2.34.5 (source: frontmatter); release metadata version 1.92.109

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
