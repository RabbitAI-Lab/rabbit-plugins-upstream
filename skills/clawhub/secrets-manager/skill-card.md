## Description:

Encrypted local secret store for OpenClaw agents that uses AES-256-GCM authenticated encryption to store, retrieve, list, rotate, audit, and delete secrets without writing plaintext secrets to disk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage local encrypted secrets, including storing, retrieving masked values, rotating credentials, auditing stale or weak secrets, and deleting entries. It is intended for trusted single-user or single-agent environments where filesystem permissions and master-key handling are acceptable controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user or agent with access to the same process and files can read stored secrets because the skill has no per-secret access-control boundary.

Mitigation: Use only in trusted single-user or single-agent environments and rely on restrictive filesystem permissions for the secrets directory and master key.

Risk: Losing .master-key makes encrypted secrets unrecoverable.

Mitigation: Back up .master-key securely and store the backup separately from routine logs or shared workspaces.

Risk: Using SECRETS_MASTER_KEY in shared, logged, containerized, or CI environments can expose the master key.

Mitigation: Prefer the file-based .master-key on a trusted host and avoid setting SECRETS_MASTER_KEY where environment variables may be observed or logged.

Risk: Raw secret output can leak through terminal scrollback, logs, transcripts, or redirected files.

Mitigation: Use masked output by default and use raw output only with explicit confirmation when piping directly to a private consuming process.

Risk: Deleting a secret is irreversible without a backup of the encrypted store.

Mitigation: Back up secrets.json before deleting secrets that may need recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-manager)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Plain text CLI output with masked values by default, optional raw stdout only with explicit confirmation, and local encrypted JSON storage files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores encrypted secrets and the master key under the configured secrets directory with restrictive file permissions where supported.]

## Skill Version(s):

1.1.18 (source: server release metadata and clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
