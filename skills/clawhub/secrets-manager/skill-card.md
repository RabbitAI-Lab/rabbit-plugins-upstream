## Description: <br>
Secrets Manager is an encrypted local secret store for OpenClaw agents that stores, retrieves, lists, rotates, audits, and deletes AES-256-GCM encrypted secrets while masking values by default. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to manage local OpenClaw secrets with encrypted storage, masked retrieval, rotation tracking, and audit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaintext secrets can be exposed when --get --raw or audit output is captured in logs, transcripts, shell history, or redirected files. <br>
Mitigation: Use masked retrieval by default, reserve --get --raw for private process handoff, and avoid writing secrets or audit output to shared or logged locations. <br>
Risk: The local .master-key file is required to recover stored secrets; losing it makes encrypted secrets unrecoverable. <br>
Mitigation: Back up .master-key securely and keep file permissions restricted to the local user. <br>
Risk: Using SECRETS_MASTER_KEY in shared, containerized, CI, or logged environments can expose the master key. <br>
Mitigation: Prefer the chmod 0600 file-based master key on a single-user host and use environment overrides only for tightly controlled ephemeral workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/secrets-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores encrypted secrets and a local master key in chmod 0600 files; raw secret retrieval prints plaintext only when explicitly requested.] <br>

## Skill Version(s): <br>
1.1.15 (source: server release evidence, clawhub.yaml, changelog released 2026-08-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
