## Description:

cloudbase helps agents develop, design, build, deploy, debug, migrate, and troubleshoot CloudBase projects across web, WeChat Mini Program, mobile, databases, cloud functions, CloudRun, storage, AI model calls, agents, operations, and specs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use cloudbase to route CloudBase work to focused references and produce implementation guidance, code, shell commands, configuration, deployment steps, reviews, and troubleshooting plans for CloudBase applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some copyable authentication and deployment examples can weaken access controls if applied directly to real CloudBase resources.

Mitigation: Review before installing when the agent may change CloudBase resources, and require explicit EnvId confirmation plus approval before deployments, permission changes, model changes, or public exposure.

Risk: Examples for token guards, anonymous auth fallback, public allow-all rules, or raw identifier logging may be unsafe in production.

Mitigation: Replace examples with real token validation, least-privilege access rules, and privacy redaction before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase scenarios](references/scenarios.md)
- [Deployment workflow](references/deployment-workflow.md)
- [MCP setup](references/mcp-setup.md)
- [CloudBase CLI](references/cloudbase-cli/SKILL.md)
- [CloudBase code review](references/cloudbase-code-review/SKILL.md)
- [Web development](references/web-development/SKILL.md)
- [CloudBase agent](references/cloudbase-agent/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and structured implementation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase resource, deployment, security-rule, and verification guidance scoped to the user's requested project.]

## Skill Version(s):

1.92.49 (source: server release metadata; artifact frontmatter reports 2.25.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
