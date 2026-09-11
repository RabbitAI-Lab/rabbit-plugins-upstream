## Description:

Manage, orchestrate, inspect, and automate the Orca IDE and Multi-Agent Runtime Server for projects, worktrees, supervised workers, terminals, decision gates, accounts, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Orca IDE runtime environments, worktrees, terminals, service health, and multi-agent orchestration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure or unsafe credential reuse when configuring Habilis, GitHub, OpenAI, Meta, Stripe, or other services.

Mitigation: Keep live tokens out of chat, store credentials in local environment or vault configuration, rotate any credential matching the published admin password or used in a URL, and use dedicated low-privilege tokens.

Risk: Privileged Orca operations can restart services, remove worktrees, send terminal input, or control workers.

Mitigation: Confirm service restarts, worktree removal, terminal-send, and worker-control actions before running them, especially on shared or production systems.

Risk: Copying root GitHub credentials into the orca account can broaden credential access.

Mitigation: Prefer authenticating GitHub directly as the orca user with scoped credentials instead of copying root credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/orca-control)
- [Publisher profile](https://clawhub.ai/user/rafacpti23)
- [Source homepage](https://github.com/rafacpti23/orca-control-skill)
- [Habilis MCP Gateway](https://xvix.com.br)
- [Orca Command Reference Cheatsheet](references/commands_cheatsheet.md)
- [Orca GitHub Integration and Preflight Diagnostics](references/github_integration_and_preflight.md)
- [Habilis SaaS and MCP Gateway Architecture Pattern](references/habilis_saas_mcp_gateway.md)
- [Thin-Skill Architecture and Multi-Client Distribution Pattern](references/thin_skill_distribution_pattern.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that inspect or change local Orca services, worktrees, terminals, accounts, and MCP configuration.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
