## Description:

Install and use the RunAPI CLI for one-off artifacts and results from registered CLI-backed services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect installed RunAPI CLI services, submit supported one-off tasks with JSON request bodies, wait for results, and verify returned artifacts. Application and production integrations should use a RunAPI SDK instead of this CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The headless install path pipes a remote installer script into the current shell.

Mitigation: Prefer `brew install runapi-ai/tap/runapi` or a verified release artifact; review the installer source before using the curl installer.

Risk: RunAPI API keys, saved credentials, listener signing secrets, and uploaded or generated files are sensitive.

Mitigation: Use environment variables or stdin token import for credentials, keep listener secrets out of logs and project config, and store generated deliverables in durable private storage when needed.

## Reference(s):

- [RunAPI model and CLI catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect current CLI help, use environment or saved authentication, and verify generated files before treating tasks as complete.]

## Skill Version(s):

0.2.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
