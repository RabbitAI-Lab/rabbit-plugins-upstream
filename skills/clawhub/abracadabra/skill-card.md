## Description:

Abra helps agents operate the abracadabra local secrets vault for scoped secret discovery, retrieval, key management, health checks, sync, cartridge checkpoints, and Touch ID-gated treasury payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[userdefault13](https://clawhub.ai/user/userdefault13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Abra when a task explicitly involves the abracadabra vault and the human has granted scoped access. It guides agents to load only approved secrets, manage key scope, inspect vault health, and request human-approved payments without exposing secret values in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may access secrets that are outside the current task or beyond the intended project scope.

Mitigation: Use only human-issued scoped keys or Touch ID-approved MCP grants, fetch only task-required key names, and stop on 401, 403, or 404 responses instead of trying alternate access paths.

Risk: Secret values or ABRA_KEY tokens could be exposed through chat, logs, command arguments, files, or process environments.

Mitigation: Never print secret values, keep bearer tokens out of command-line arguments, avoid writing fetched secrets to disk, and inject only explicitly allowlisted names into trusted child processes.

Risk: Vault responses or secret values could be misused as executable code or shell input.

Mitigation: Treat API and MCP responses as opaque data, parse them with fixed JSON handling, reject dangerous environment names, and never evaluate or pipe vault data into a shell.

Risk: LAN vault access or treasury payment flows could expose credentials or spend funds without appropriate human control.

Mitigation: Require API keys for off-loopback secret access, use TLS verification for LAN mode, check treasury status before payment requests, and proceed with payments only after explicit Touch ID approval.

## Reference(s):

- [Abra Skill Page](https://clawhub.ai/userdefault13/skills/abracadabra)
- [Abracadabra Distribution Docs](https://github.com/userdefault13/AarcadeGh-t/blob/main/docs/ABRACADABRA-DIST.md)
- [Abracadabra Cartridge Docs](https://github.com/userdefault13/abracadabra/blob/main/docs/CARTRIDGE.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Code]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to avoid printing secret values and to confirm only key names or safe prefixes when necessary.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
