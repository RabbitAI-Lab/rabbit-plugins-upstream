## Description:

CloudBase guides agents through building, deploying, debugging, migrating, and troubleshooting Tencent CloudBase projects across web apps, WeChat mini programs, authentication, databases, cloud functions, CloudRun, storage, AI model integration, agents, operations, and specs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to route CloudBase work to the right local guidance, prepare CloudBase resources, generate or update application code, deploy services, and verify CloudBase-specific behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marked the skill suspicious because auth, agent, deployment, and command examples could lead to unsafe production behavior if followed automatically.

Mitigation: Review proposed changes before execution, confirm the target EnvId, account, and deployment scope, and avoid applying the skill to non-CloudBase work.

Risk: Generated auth, JWT, CORS, token, logging, and third-party agent examples may expose sensitive data or weaken production controls.

Mitigation: Harden generated examples before release, keep identifiers, prompts, API keys, and third-party agent data sensitive, and avoid automatic remote-download or removal commands.

## Reference(s):

- [CloudBase Skill Source](artifact/SKILL.md)
- [CloudBase Scenario Guide](artifact/references/scenarios.md)
- [Deployment Workflow](artifact/references/deployment-workflow.md)
- [MCP Setup Reference](artifact/references/mcp-setup.md)
- [Tooling Fallback Guide](artifact/references/tooling-fallback.md)
- [Console Entry Points](artifact/references/console-links.md)
- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/cloudbase)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline commands, code snippets, configuration examples, and implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include CloudBase resource, deployment, authentication, database, storage, AI integration, and troubleshooting instructions.]

## Skill Version(s):

1.92.72 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
