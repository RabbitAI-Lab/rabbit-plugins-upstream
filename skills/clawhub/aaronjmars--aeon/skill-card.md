## Description:

Aeon helps developers and operators set up, run, schedule, troubleshoot, and evolve Aeon agent instances and skills in GitHub repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aaronjmars](https://clawhub.ai/user/aaronjmars)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to bootstrap an Aeon instance, configure model and notification credentials, choose and schedule skills, debug runs, edit skill prompts, and convert recurring coding-agent work into scheduled Aeon skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: History-mining mode reads local coding-agent transcript history that may contain sensitive prompts or project context.

Mitigation: Use a narrow time window and project scope, and keep outputs to aggregate patterns rather than raw transcript content in notifications or commits.

Risk: Repository setup and secret-management guidance can affect live Aeon instances and credentials.

Mitigation: Confirm the resolved GitHub repository before writes, set secrets through stdin, and use least-privilege tokens where possible.

Risk: Tracing or observability settings can expose prompt content from sensitive work.

Mitigation: Keep tracing disabled for sensitive work, or configure content logging off before running the skill.

## Reference(s):

- [Inventory & paths](references/layout.md)
- [Aeon secrets and variables](references/secrets.md)
- [MCP servers](references/mcp.md)
- [How Aeon skills are actually written](references/skill-anatomy.md)
- [CI gates in aeonfun/aeon](references/ci.md)
- [History mining deep reference](references/history-mining.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository configuration changes, skill files, schedules, and local history-mining digests.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
