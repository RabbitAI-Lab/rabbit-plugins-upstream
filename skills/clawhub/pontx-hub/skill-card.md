## Description:

Discover, compare, inspect, preview, call, and integrate curated public APIs with Pontx Hub.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Pontx Hub to discover public APIs, inspect current endpoint and schema metadata, preview requests safely, and generate SDK-based integration code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed if copied into chat, source files, logs, or command arguments.

Mitigation: Read credentials from the environment variables declared by Pontx Hub or from a secret manager, and do not print or persist secret values.

Risk: POST, PUT, PATCH, or DELETE requests can modify external systems.

Mitigation: Preview the exact resolved request first, ask the user to confirm that unchanged request, and only then execute it with the required confirmation flag.

Risk: Stale provider-specific guidance could conflict with current endpoint, schema, authentication, package, or server metadata.

Mitigation: Treat Pontx Hub's current PontxSpec inspection as authoritative for API metadata, even when a provider-specific product Skill is installed.

## Reference(s):

- [Authentication and mutation safety](references/auth-and-safety.md)
- [Pontx Hub ClawHub page](https://clawhub.ai/pontjs/skills/pontx-hub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON-oriented CLI guidance, and generated SDK code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves CLI exit codes and machine-readable error codes when reporting failures.]

## Skill Version(s):

0.5.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
