## Description:

Growth Engineer for mobile apps and agent runtimes including OpenClaw and Hermes. Correlate analytics, crashes, billing, feedback, store signals, and repo context into proposal drafts that can flow into agent chat, GitHub issues, or draft pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wotaso-dev](https://clawhub.ai/user/wotaso-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Product engineers, growth engineers, and app maintainers use this skill to connect analytics, monetization, crash, feedback, store, and repo signals, then produce prioritized growth and production-health proposals for OpenClaw, Hermes, GitHub issues, or draft pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill can make lasting local automation changes, including tooling updates, config files, scheduler files, and external delivery artifacts.

Mitigation: Install it only in a trusted workspace, review generated config and cron settings, and enable GitHub writes or autopilot behavior only after explicit manual confirmation.

Risk: Configured connectors may use credentials for analytics, billing, crash monitoring, store, GitHub, and notification systems.

Mitigation: Use least-privilege tokens, keep secrets in the host terminal or secret store, and avoid exposing secrets in chat, repository files, logs, issue bodies, or pull request text.

Risk: Custom commands, package installs, MCP token persistence, sudo setup, or isolated-runner setup can expand local execution scope.

Mitigation: Avoid broad custom shell commands from untrusted config and require manual review before package installs, sudo actions, token persistence, or isolated-runner changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wotaso-dev/skills/growth-engineer)
- [Declared project homepage](https://github.com/Wotaso/growth-engineer-skill)
- [Advanced Setup](references/advanced-setup.md)
- [Setup And Scheduling](references/setup-and-scheduling.md)
- [Required Secrets](references/required-secrets.md)
- [Input Schema](references/input-schema.md)
- [Generated GitHub Issue Template](references/issue-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON summaries, local configuration files, shell commands, issue drafts, and optional GitHub issues or draft pull requests when configured]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local outbox, connector-health, scheduler-proof, proposal, and configuration artifacts; external delivery is configuration-dependent.]

## Skill Version(s):

1.0.210 (source: server release, SKILL.md metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
