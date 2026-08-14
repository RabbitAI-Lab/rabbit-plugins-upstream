## Description:

CloudBase helps agents develop, deploy, debug, migrate, and troubleshoot Tencent CloudBase projects across web, WeChat Mini Program, mobile, serverless, database, AI model, and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, build, configure, deploy, test, and review CloudBase-backed applications. It routes work to focused CloudBase references for authentication, databases, cloud functions, CloudRun, storage, AI model integration, operations, and specification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CloudBase changes can introduce insecure application behavior or high-impact cloud changes.

Mitigation: Review generated changes before execution, require explicit user confirmation for EnvId, billing, resource, and destructive changes, and keep endpoints private by default unless public access is intentional.

Risk: Authentication and API examples may be copied without adequate server-side validation or CORS controls.

Mitigation: Require real server-side token validation, explicit CORS origins, and private-by-default endpoint design before deployment.

Risk: Prompts, logs, JWT claims, conversation history, checkpoints, or third-party LLM calls may expose unnecessary data.

Mitigation: Minimize collected and transmitted data, avoid storing secrets or unnecessary claims, and review logging and third-party model calls for sensitive content.

Risk: Copyable command examples involving public access rules, confirm=yes flags, rm -rf, or credential and API-key flows can cause unintended changes.

Mitigation: Treat those examples as requiring explicit user intent and human review before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/cloudbase)
- [CloudBase main skill](artifact/SKILL.md)
- [CloudBase MCP setup](artifact/references/mcp-setup.md)
- [Deployment workflow](artifact/references/deployment-workflow.md)
- [CloudBase platform reference](artifact/references/cloudbase-platform/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration snippets, and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CloudBase resource-management steps, MCP or CLI instructions, generated application code, and security review guidance.]

## Skill Version(s):

1.92.52 (source: server release metadata; artifact frontmatter version 2.26.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
