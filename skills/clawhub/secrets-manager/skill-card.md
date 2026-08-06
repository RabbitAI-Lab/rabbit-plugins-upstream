## Description:

Secrets Manager provides an encrypted local secret store for OpenClaw agents using AES-256-GCM, with masked retrieval, listing, rotation, auditing, deletion, and local master-key management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to store, retrieve, rotate, audit, and delete local OpenClaw secrets without writing plaintext secrets to disk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw secret output can expose plaintext through terminal scrollback, logs, shared files, CI output, or agent transcripts.

Mitigation: Use masked retrieval by default, avoid --get --raw unless necessary, and never redirect plaintext secrets into shared locations such as /tmp.

Risk: Stored secrets are readable by any trusted local agent or process that can access the secret store and master key.

Mitigation: Install only inside a trusted local agent/process boundary and keep the chmod 0600 secret data and .master-key files private.

Risk: Loss or exposure of .master-key can make secrets unrecoverable or compromise all stored secrets.

Mitigation: Back up .master-key securely and avoid using SECRETS_MASTER_KEY in shared, containerized, CI, or logged environments.

Risk: Delete and rotate operations can remove active values or change credentials unexpectedly.

Mitigation: Require explicit user intent before delete or rotate operations and review downstream consumers before rotating secrets.

## Reference(s):

- [Secrets Manager ClawHub listing](https://clawhub.ai/jlacroix82/skills/secrets-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and text command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Masked secret values are the default; raw plaintext can be emitted only when --get --raw is explicitly used.]

## Skill Version(s):

1.1.17 (source: server release metadata and CHANGELOG.txt, released 2026-08-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
