## Description:

CloudBase helps agents build, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across web, mini program, mobile, backend, database, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local reference, prepare CloudBase resources, implement application changes, deploy web or backend components, and troubleshoot platform issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward CloudBase resource management and deployment actions that affect environments, costs, public endpoints, or production services.

Mitigation: Require explicit user confirmation for environment selection, paid operations, production changes, public endpoints, and delete or overwrite actions.

Risk: Copied authentication, logging, LLM, or observability examples may be unsuitable for production without review.

Mitigation: Treat examples as templates and perform security review before production use, especially for auth flows, privacy-sensitive logs, and model integration.

Risk: The activation scope is broad and could be applied outside a CloudBase project.

Mitigation: Confirm the project uses CloudBase before applying this skill, and avoid using it for pure frontend or self-hosted backend work without CloudBase.

## Reference(s):

- [CloudBase skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [Activation map](references/activation-map.yaml)
- [CloudBase scenarios](references/scenarios.md)
- [Deployment workflow](references/deployment-workflow.md)
- [MCP setup](references/mcp-setup.md)
- [Tooling fallback](references/tooling-fallback.md)
- [Console links](references/console-links.md)
- [CloudBase pricing](https://cloud.tencent.com/document/product/876/75213)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scenario-dependent and may include design specs, deployment steps, CloudBase resource changes, review findings, and troubleshooting guidance.]

## Skill Version(s):

1.92.62 (source: server release metadata); artifact frontmatter reports 2.28.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
