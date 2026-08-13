## Description:

Detects partially wiped agent workspaces, verifies file, blob, and tree integrity, and guides signed repair workflows with optional encrypted off-box manifest sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to detect workspace damage after partial filesystem persistence, repair damaged entries in dependency order, and recover signed manifests when local state is lost. It is suited to sandboxes where build outputs, virtual environments, models, credentials, or executable bits may disappear between turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manifest entries can lead to shell command execution, including a disclosed check path that may execute manifest-provided commands without the restore signature guard.

Mitigation: Review manifest entries as executable code and only run check, doctor, restore, or the turn-start hook after verifying the signer or digest and accepting the listed commands.

Risk: Manifests from paste URLs or peers may contain delete, download, credential, smoke-test, or shell commands that are unsafe for the current workspace.

Mitigation: Inspect untrusted manifests before use, prefer trusted signers or exact digest approval, and avoid automated turn-start execution for peer or paste-sourced manifests until reviewed.

Risk: Off-box recovery sync can expose sensitive recovery metadata or secrets if used in plaintext or with insufficient review.

Mitigation: Use encrypted sync or strict redaction, verify paste hashes on pull, and avoid plaintext publication unless the manifest has been confirmed clean.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience)
- [Publisher Profile](https://clawhub.ai/user/orionshaowswmw)
- [Manifest Example](artifact/reference/manifest.example.json)
- [Turn Start Hook](artifact/reference/turn-start-hook.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON manifest examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands can emit status reports and JSON; repair behavior depends on user-reviewed manifest entries and local environment variables.]

## Skill Version(s):

1.4.9 (source: server release evidence; artifact documentation reports 1.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
