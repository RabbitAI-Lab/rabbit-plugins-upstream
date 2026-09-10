## Description:

Manage, orchestrate, inspect, and automate the Orca IDE and Multi-Agent Runtime Server - projects, worktrees, supervised workers, interactive terminals, decision gates, accounts, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0 License

## Use Case:

Developers and engineering operators use this skill to inspect and operate Orca runtime services, manage projects and worktrees, supervise multi-agent tasks, control terminals, and trigger automations. It is intended for normal ClawHub use, with elevated care because it can send terminal commands, restart services, and handle credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that documentation exposes a real-looking admin password.

Mitigation: Review and remove exposed operational secrets before installation, and rotate the password if it was ever real.

Risk: The skill can send terminal commands and restart runtime services.

Mitigation: Confirm target terminals, worktrees, services, and commands before execution, especially for service restarts or automation triggers.

Risk: The security guidance warns against copying root GitHub credentials into Orca.

Mitigation: Use dedicated least-privilege service accounts and authenticate credentials under the intended Orca user context.

Risk: The security guidance flags unpinned MCP client package execution with bearer tokens.

Mitigation: Pin MCP client packages and protect bearer tokens in environment variables or managed secret storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/orca-control)
- [Project homepage](https://github.com/rafacpti23/orca-control-skill)
- [Orca Command Reference Cheatsheet](references/commands_cheatsheet.md)
- [Orca GitHub Integration & Preflight Diagnostics](references/github_integration_and_preflight.md)
- [Habilis SaaS & MCP Gateway Architecture Pattern](references/habilis_saas_mcp_gateway.md)
- [Thin-Skill Architecture & Multi-Client Distribution Pattern](references/thin_skill_distribution_pattern.md)
- [Orca environment check script](scripts/orca-env-check.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational commands for Orca services, terminals, worktrees, automations, accounts, GitHub preflight checks, and MCP gateway configuration.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
