## Description:

Detect and repair partially wiped agent workspaces with integrity checks, signed manifests, guarded restore recipes, bounded local recovery state, and explicit off-box sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to detect missing, truncated, corrupted, or permission-stripped workspace assets and to run reviewed recovery plans for files, trees, models, scripts, and build outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restore recipes, smoke commands, and exported shell runbooks can execute shell behavior after approval.

Mitigation: Review every command before signing, use --dry-run on new manifests, and approve only exact manifest digests that match the intended recovery plan.

Risk: Cleartext off-box manifest sync can expose recovery details or sensitive content.

Mitigation: Prefer encrypted sync for sensitive manifests, avoid cleartext paste sync, and never upload inline escrow content without encryption.

Risk: Local signing and identity files protect trust decisions and can be misused if exposed.

Mitigation: Keep ~/.swr signing, trust, and identity files private and verify public-key fingerprints out of band before trusting another signer.

Risk: Performance-oriented cache and sampled checks are not a substitute for high-assurance verification or backups.

Mitigation: Use --no-cache and content hashing when assurance matters, and keep normal backups, immutable copies, access controls, and rehearsed recovery plans for important data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/snapshot-wipe-resilience)
- [Manifest example](reference/manifest.example.json)
- [Turn-start hook example](reference/turn-start-hook.sh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON status reports, shell command examples, configuration manifests, and recovery plan exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local integrity reports, guarded restore plans, and optional shell or Markdown recovery runbooks; network sync is explicit and not required for local checks.]

## Skill Version(s):

1.5.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
