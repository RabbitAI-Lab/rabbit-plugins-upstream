## Description:

AgentKey is a local, offline, encrypted API-key vault for agents that supports add, get, rotate, list, audit, status, and report workflows with redacted outputs and tamper detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use AgentKey to store and retrieve API keys locally, rotate credentials, inspect redacted inventories, and gate sessions on key freshness or audit integrity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vault can be pointed at an alternate local OpenSSL executable, which could expose the vault passphrase if the environment is influenced.

Mitigation: Do not set AGENTKEY_OPENSSL_BIN in normal use, run the skill in a controlled local environment, and keep AGENTKEY_HOME and passphrase files private.

Risk: The previous encrypted key is intentionally retained after rotation, extending the period in which an old credential remains recoverable.

Mitigation: Remove the .prev encrypted key file after confirming the rotated credential works.

Risk: The audit log is a local consistency check and should not be treated as a tamper-proof record.

Mitigation: Use audit verification as a local warning signal and pair it with normal host, filesystem, and backup controls for higher-assurance environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agentkey)
- [Operations guide](artifact/docs/operations.md)
- [Security evidence](artifact/docs/evidence.md)
- [Integration guide](artifact/docs/integration.md)
- [Machine-readable manifest](artifact/manifest.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; CLI outputs JSON for inventory, status, audit, and report commands, and raw text only for key retrieval.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redacted outputs are used for list, status, audit, report, and fingerprint flows; direct key material is only produced by get.]

## Skill Version(s):

2.0.0 (source: frontmatter, changelog, manifest, server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
