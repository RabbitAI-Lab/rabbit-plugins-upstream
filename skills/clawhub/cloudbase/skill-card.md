## Description:

CloudBase helps agents build, deploy, debug, and troubleshoot CloudBase web, WeChat mini program, mobile, backend, database, storage, authentication, AI, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to select the right CloudBase guidance, prepare cloud resources, implement app features, deploy services, and troubleshoot CloudBase projects across web, mini program, mobile, serverless, CloudRun, database, storage, authentication, AI, and operations scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad CloudBase management and deployment actions.

Mitigation: Install it only for agents that should manage CloudBase resources, and review proposed cloud operations before execution.

Risk: Commands or generated configuration may target the wrong CloudBase environment.

Mitigation: Confirm the exact EnvId before cloud operations and avoid relying on implicit or selected environment state.

Risk: Persistent user-level tooling setup can change future agent capabilities.

Mitigation: Prefer scoped plugin targets and pinned package versions where possible.

Risk: Secrets or privileged keys could be exposed through chat, browser code, or generated configuration.

Mitigation: Do not paste long-lived secrets into chat, and do not expose service-role or API keys to browser code.

Risk: Force or auto-confirm flags can bypass interactive review.

Mitigation: Reserve `--yes` and `--force` for controlled CI contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase scenarios](references/scenarios.md)
- [Deployment workflow](references/deployment-workflow.md)
- [MCP setup](references/mcp-setup.md)
- [MCP vs CLI tooling fallback](references/tooling-fallback.md)
- [CloudBase console entry points](references/console-links.md)
- [Activation map](references/activation-map.yaml)
- [CloudBase Pricing](https://cloud.tencent.com/document/product/876/75213)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide cloud-management actions; users should confirm EnvId values, credentials, and production changes before execution.]

## Skill Version(s):

1.92.81 (source: server release metadata; artifact frontmatter version is 2.33.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
