## Description:

Build or modernize TypeScript CLIs for AI agents with @renxqoo/agent-cli-sdk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[renxqoo](https://clawhub.ai/user/renxqoo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, extend, test, package, and document production-style TypeScript CLIs that AI agents can call reliably.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CLI work can involve package installation, global writes, login or registration flows, network calls, or data-changing operations.

Mitigation: Review those actions before execution and require authorization for install, login, live API, global write, or mutation steps.

Risk: Credentials or sensitive responses could be exposed if copied into chat, command arguments, logs, examples, or snapshots.

Mitigation: Keep real credentials out of chat and command arguments, use local terminal flows for registration, and redact diagnostic output.

Risk: Generated commands or documentation can be incorrect when API fields, authentication requirements, scopes, pagination, or error contracts are unverified.

Mitigation: Derive those details from verified contracts, tests, or real authorized responses, and mark unresolved facts as explicit blockers instead of guessing.

## Reference(s):

- [Agent CLI Builder on ClawHub](https://clawhub.ai/renxqoo/skills/agent-cli-builder)
- [Core Implementation Contract](references/core-api.md)
- [Authentication with defineAuth](references/auth-patterns.md)
- [Custom Authentication Plugins and Providers](references/custom-auth-plugin.md)
- [Error Catalog and Status Mapping](references/error-catalog.md)
- [Advanced Patterns: Pagination, Pipes, and Human Output](references/patterns.md)
- [Plugin Patterns and Hook Ordering](references/plugin-patterns.md)
- [JSON arguments and write safety](references/structured-input.md)
- [Skill Generation, Synchronization, and Distribution](references/skill-gen.md)
- [Production Skill Optimization Guide](references/skill-optimization.md)
- [README Generation Guide](references/readme-gen.md)
- [Testing and Real-Task Evaluation](references/testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with code blocks, shell commands, configuration snippets, and validation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed file edits, package scripts, CLI invocations, tests, README or Skill content, and explicit blockers for unverified facts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
