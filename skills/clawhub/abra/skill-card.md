## Description:

Operate the abracadabra local secrets vault through the abra CLI, server, or MCP for scoped secret access, key management, sync/checkpoint operations, and treasury payments without printing secret values in chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[userdefault13](https://clawhub.ai/user/userdefault13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to work with a local abracadabra secrets vault, loading only human-scoped secrets into processes or configuration and managing related vault operations without exposing secret values in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive vault secrets, API keys, passwords, private keys, and payment-related treasury actions.

Mitigation: Install only when intentionally using abracadabra, keep keys narrowly scoped and expiring, prefer MCP approval or no-file environment injection, and never print or log secret values.

Risk: Writing fetched secrets to files can leave sensitive material on disk.

Mitigation: Avoid the private-file workflow when possible; when a file is unavoidable, write outside the repository with restrictive permissions and delete it promptly.

Risk: Passing vault tokens or secret payloads through command arguments, insecure LAN TLS, or shell evaluation can expose credentials.

Mitigation: Pass secrets only to trusted commands, keep bearer keys out of process arguments, prefer loopback access, require scoped API keys off-loopback, and never execute vault responses as code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/userdefault13/skills/abra)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should name loaded secret keys only and avoid printing secret values, vault tokens, private keys, or environment contents.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
