## Description: <br>
Full SSH remote execution with sudo support, password authentication, vault integration, ControlMaster multiplexing, and an environment-level dangerous-operations gate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run supervised SSH commands, inspect remote Linux hosts, manage credential-backed access, and perform sudo-enabled maintenance when explicitly approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The full edition supports sudo and SSH password authentication; the security summary says sudo password handling can expose credentials despite safer-handling claims. <br>
Mitigation: Prefer the base key-only edition unless sudo or password authentication is specifically needed; avoid password-based sudo where possible and use safer approval and password-passing designs. <br>
Risk: Host-key, key-restore, and cleanup paths can increase exposure if operators relax verification or run file operations with elevated privileges. <br>
Mitigation: Keep host-key checking strict, use ssh-agent for private keys, and avoid cleanup or restore-to-file paths with elevated privileges unless target files and hosts have been verified. <br>
Risk: Remote execution can modify systems or expose sensitive operational data. <br>
Mitigation: Start with read-only inspection, require explicit approval for mutating commands and sudo, and redact sensitive log or credential-adjacent output before sharing. <br>


## Reference(s): <br>
- [SSH Executor Safety Notes](references/safety.md) <br>
- [ClawHub Security Audit - July 2026](references/security-audit-2026-07-clawhub.md) <br>
- [Vault Backend Integration](references/vault-backends.md) <br>
- [Vaultwarden + SSH Agent Integration](references/vault-ssh-integration.md) <br>
- [SSH Key Format in Vaultwarden](references/vault-key-format.md) <br>
- [Multiplexing Verification](references/multiplexing-verification.md) <br>
- [Docker Diagnostics Without Docker CLI](references/docker-diagnostics-without-cli.md) <br>
- [Server-to-Server rsync via Temporary Key](references/server-to-server-rsync.md) <br>
- [Remote Backup Cleanup via SSH](references/remote-backup-cleanup.md) <br>
- [Testing Pitfalls - Discovered 2026-07-23](references/testing-pitfalls-2026-07-23.md) <br>
- [Troubleshooting Field Notes](references/troubleshooting-field-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote command wrappers return parseable JSON on stdout while status and warnings are written to stderr.] <br>

## Skill Version(s): <br>
2.4.2 (source: server release metadata and artifact release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
