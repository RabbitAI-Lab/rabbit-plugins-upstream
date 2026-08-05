## Description:

CloudBase guides agents through developing, deploying, debugging, and operating Tencent CloudBase projects across web, mini program, backend, database, auth, storage, AI, and agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase tasks to the right local references and receive implementation, deployment, troubleshooting, and review guidance for CloudBase-backed applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt an agent to install plugins, call CloudBase MCP tools, mutate cloud resources, expose public endpoints, or run local deletion and rebuild commands too readily.

Mitigation: Require explicit approval before plugin installation, CloudBase MCP calls, environment creation or renewal, permission changes, public endpoint exposure, and shell commands that delete or rebuild local directories.

Risk: Auth, CORS, logging, JWT, and public-access examples may be unsuitable as production defaults.

Mitigation: Treat these examples as templates and require production security review before copying them into deployed systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase entry skill](artifact/SKILL.md)
- [Activation map](artifact/references/activation-map.yaml)
- [MCP setup](artifact/references/mcp-setup.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase platform guide](artifact/references/cloudbase-platform/SKILL.md)
- [CloudBase code review guide](artifact/references/cloudbase-code-review/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code, shell commands, configuration snippets, and file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CloudBase management steps, deployment guidance, code review findings, and explicit approval gates for risky actions.]

## Skill Version(s):

1.92.46 (source: server release metadata; artifact frontmatter version: 2.25.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
