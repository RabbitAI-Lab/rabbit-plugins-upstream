## Description:

Detects and repairs partially wiped agent workspaces with integrity checks, signed manifests, guarded restore recipes, bounded local recovery state, and explicit off-box sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent maintainers use this skill to detect workspace state loss, verify files or trees against a healthy manifest, and run reviewed recovery plans when agent workspaces lose integrity between turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed restore recipes and smoke commands can execute shell code that changes files, uses credentials, or makes network requests.

Mitigation: Review each manifest command before signing or approving it, run dry-run first, and scope the workspace narrowly.

Risk: Off-box manifest sync may expose sensitive paths, recipes, or escrowed content if used without appropriate protection.

Mitigation: Use encrypted sync for sensitive manifests and avoid cleartext publication unless the manifest has been reviewed for disclosure.

Risk: Recovery checks are not a substitute for durable backups or access controls.

Mitigation: Use this skill as a workspace repair aid alongside normal backup, immutable-copy, access-control, and disaster-recovery practices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience)
- [Manifest example](reference/manifest.example.json)
- [Turn-start hook example](reference/turn-start-hook.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON reports, shell commands, and recovery plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local integrity reports, signed recovery plans, and operator-reviewed restore or sync commands.]

## Skill Version(s):

1.5.6 (source: server release metadata, SKILL.md, README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
