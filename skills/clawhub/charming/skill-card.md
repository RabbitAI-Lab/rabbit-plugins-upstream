## Description:

Build, inspect, update, and call hosted personal apps with the Charming CLI. Covers the app contract (manifest, capabilities, env.storage, routes, window.charming.api), the sandbox rules, and the CLI workflow. Use when a user wants to create or manage an interactive personal app hosted by Charming.

This skill is ready for commercial/non-commercial use.

## Publisher:

[charming](https://clawhub.ai/user/charming)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, inspect, update, call, share, and delete hosted personal apps through the Charming CLI. It is intended for workflows that need guidance on the app manifest, storage, routes, UI runtime, sandbox rules, and CLI lifecycle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through creating or replacing hosted apps, changing sharing settings, and deleting apps.

Mitigation: Run dry-runs first, keep explicit user approval before replacement, public sharing, or deletion, and review mutation commands before execution.

Risk: Authentication and credential workflows can expose sensitive values if handled carelessly.

Mitigation: Do not print tokens or device codes; show only the login user code when needed and follow the CLI recovery guidance for errors.

Risk: Hosted apps may persist or share user data.

Mitigation: Store user data in env.storage, avoid embedding real user data in source constants, and review public sharing, secrets, and app source before publication.

## Reference(s):

- [Charming skill page](https://clawhub.ai/charming/skills/charming)
- [Charming publisher profile](https://clawhub.ai/user/charming)
- [Charming website](https://usecharming.com)
- [Charming app manifest schema](https://charm.ing/schema/app-manifest/2026-07-31.json)
- [App contract](resources/contract.md)
- [Patterns worth reusing](resources/patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run commands, app source edits, route-call examples, and review guidance for hosted app mutations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
