## Description: <br>
Execute commands on remote hosts over SSH with structured discovery, pluggable credential backends, and safety guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect and administer remote Linux hosts over SSH, including structured discovery of host identity, runtime, network, storage, and service state. It can propose guarded command execution workflows for read-only inspection and explicitly approved maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security verdict is suspicious because sudo password handling can expose passwords and needs review before installation. <br>
Mitigation: Install only when the Full edition's sudo or password features are required; prefer the base/key-only edition or narrowly scoped NOPASSWD commands where possible. <br>
Risk: Password-based SSH and sudo operations increase credential exposure risk. <br>
Mitigation: Require explicit user approval and the SSH_EXECUTOR_ALLOW_DANGEROUS=1 environment opt-in before password or sudo execution. <br>
Risk: Remote command execution can mutate or damage systems if an unsafe command is approved. <br>
Mitigation: Start with read-only inspection, show the exact command before mutation, and require confirmation for sudo, destructive commands, package changes, service changes, data deletion, and network changes. <br>
Risk: Temporary SSH key files can persist if cleanup is interrupted. <br>
Mitigation: Prefer ssh-agent or vault-backed key loading; use cleanup routines and verify removal when temporary key material is unavoidable. <br>
Risk: Host-key bypass can expose sessions to impersonation or man-in-the-middle attacks. <br>
Mitigation: Keep strict host-key verification enabled by default and require explicit fingerprint verification before first contact with unknown hosts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rickkbarbosa/skills/ssh-executor) <br>
- [SSH Executor Safety Notes](references/safety.md) <br>
- [ClawHub Security Audit - July 2026](references/security-audit-2026-07-clawhub.md) <br>
- [Vault Backend Integration](references/vault-backends.md) <br>
- [Vaultwarden + SSH Agent Integration](references/vault-ssh-integration.md) <br>
- [Multiplexing Verification](references/multiplexing-verification.md) <br>
- [Server-to-Server rsync via Temporary Key](references/server-to-server-rsync.md) <br>
- [Docker Diagnostics Without Docker CLI](references/docker-diagnostics-without-cli.md) <br>
- [Remote Backup Cleanup via SSH](references/remote-backup-cleanup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result contracts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command wrappers return parseable JSON on stdout and status or warning text on stderr.] <br>

## Skill Version(s): <br>
2.4.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
