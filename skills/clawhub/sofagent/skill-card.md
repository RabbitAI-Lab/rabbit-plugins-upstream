## Description:

FDE Harness helps field deployment engineers guide enterprise AI rollouts by constraining agent behavior, auditing changes, capturing lessons, and producing enterprise-specific skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Field deployment engineers, enterprise IT teams, and agent developers use this skill to assess business workflows, identify AI-suitable nodes, quantify value, configure audit and governance controls, and hand over maintainable enterprise skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad execution, persistence, and agent-behavior authority can affect future agent sessions if installed without clear scope.

Mitigation: Install only in controlled enterprise or test environments, define the allowed scope before activation, and review generated skills, custom prompt layers, MCP configuration, and .sofagent files before reuse.

Risk: Installation and runtime flows reference shell commands and npx/npm packages that could execute changing third-party code.

Mitigation: Review install scripts and external packages before use, pin package versions, and require human approval before executing installation, daemon, restore, or deployment commands.

Risk: Daemon or scheduled jobs may continue to run audits, health checks, or knowledge extraction beyond the immediate task.

Mitigation: Disable background jobs by default unless needed, document their cadence and data access, and periodically verify that scheduled jobs remain necessary and appropriately scoped.

Risk: Passing raw user text through shell-oriented commands can create command-injection or unintended execution paths.

Mitigation: Do not pass untrusted user text directly to shell commands; quote or parameterize inputs and prefer reviewed wrappers for task execution.

## Reference(s):

- [FDE Harness ClawHub release](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Agency Agents code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, structured reports, and generated skill or handoff content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include enterprise workflow notes, audit summaries, handoff documents, generated skill instructions, and local configuration guidance.]

## Skill Version(s):

1.4.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
