## Description:

Snapshot-Wipe Resilience helps agents detect and repair partially wiped workspaces by checking file, blob, and tree integrity, then restoring damaged entries from signed manifests and optional encrypted off-box sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to keep volatile agent workspaces recoverable across turns. It is intended for health checks, manifest-based repair, portable runbook export, and recovery after files, dependencies, models, scripts, or credentials disappear or lose integrity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restore recipes, smoke tests, exported runbooks, and pulled manifests can behave like executable code.

Mitigation: Review manifests and recipes before use, prefer read-only checks or doctor --dry-run first, and sign manifests you authored.

Risk: Automatic repair can replace files or run stored shell commands if restore-oriented commands are enabled.

Mitigation: Audit destructive recipes before enabling restore flows or the turn-start hook, and avoid --i-trust-this-manifest unless the exact digest has been reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience)
- [README](README.md)
- [Example recovery manifest](reference/manifest.example.json)
- [Turn-start hook example](reference/turn-start-hook.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON manifests, and shell or Markdown recovery runbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit JSON status for agent consumption and can execute restore recipes when the user runs restore-oriented commands]

## Skill Version(s):

1.4.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
