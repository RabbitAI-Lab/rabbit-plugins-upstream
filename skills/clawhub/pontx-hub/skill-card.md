## Description:

Search, inspect, preview, call, and integrate curated public APIs through Pontx Hub for catalog-wide API discovery, PontxSpec Endpoint or Schema inspection, product Skill installation, safe request preview, explicit mutation confirmation, and unified SDK integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use Pontx Hub to discover curated public APIs, inspect current PontxSpec endpoint and schema metadata, preview requests safely, install focused product Skills when useful, and generate SDK-based integration code after request shapes are verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent execute real provider API calls, including mutations.

Mitigation: Use preview first, present the resolved method, host, path, query, redacted headers, body, and expected side effect, and require explicit confirmation before any POST, PUT, PATCH, or DELETE call.

Risk: Credentials could be exposed if placed in command arguments, generated examples, source files, or chat messages.

Mitigation: Read secrets only from the environment variables declared by the catalog, redact credentials in previews and reports, and avoid writing secret values into generated content.

Risk: Stale provider-specific details can lead to incorrect endpoint, authentication, package, or server metadata.

Mitigation: Inspect the current PontxSpec through Pontx Hub for authoritative endpoint, schema, authentication, package, and server details; use product Skills only for provider-specific workflow guidance.

## Reference(s):

- [Pontx Hub ClawHub release](https://clawhub.ai/pontjs/skills/pontx-hub)
- [Authentication and mutation safety](references/auth-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers --json for programmatic CLI output, preserves CLI exit codes and machine-readable error codes, and keeps credentials out of command arguments and generated examples.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
