## Description:

Writes, runs, and debugs end-to-end tests for web and mobile apps, including agent-assisted UI testing and app exploration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to create, run, and troubleshoot end-to-end tests for web and mobile apps, inspect running app behavior, and explore flows for bugs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous exploration and automatic upgrades may cause consequential app or dependency changes without consistent limits.

Mitigation: Use disposable test accounts and synthetic data in an isolated app; set explicit limits on purchases, account changes, and administrative actions. Review upgrades separately and prefer locked local executables.

Risk: Screen content sent to a configured model and unmasked CI videos or diagnostics may expose sensitive information.

Mitigation: Review what screen content reaches the model and restrict access to CI diagnostics, especially unmasked videos.

## Reference(s):

- [e2e homepage](https://e2e.com)
- [Setup](references/setup.md)
- [Writing tests](references/writing-tests.md)
- [Agent steps](references/agent.md)
- [Running tests](references/running.md)
- [Debugging](references/debugging.md)
- [Exploring an app](references/explore.md)
- [Driving the app over MCP](references/mcp.md)
- [Running a bug bash](references/bug-bash.md)
- [Decision models](https://e2e.com/docs/decision-models)
- [Agent documentation](https://e2e.com/docs/agents)
- [AI SDK providers](https://ai-sdk.dev/providers)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Testing guidance]

**Output Format:** [Markdown guidance with code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific test and configuration examples.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
