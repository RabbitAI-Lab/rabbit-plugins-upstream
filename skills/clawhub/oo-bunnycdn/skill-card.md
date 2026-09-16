## Description:

BunnyCDN (bunny.net). Use this skill for BunnyCDN requests including reading Pull Zones, listing Pull Zones, and purging Pull Zone caches through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect BunnyCDN Pull Zones and purge Pull Zone cache entries from an agent workflow. It is intended for accounts already connected through OOMOL, with destructive cache purge actions requiring explicit target confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts without a built-in verification step.

Mitigation: Review the installer path before installing; prefer a versioned, verified source or manually inspect and verify the downloaded installer before execution.

Risk: The purge_pull_zone_cache action can remove cached BunnyCDN content.

Mitigation: Confirm the exact Pull Zone and optional cache tag with the user before allowing the purge action to run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bunnycdn)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [BunnyCDN Homepage](https://bunny.net/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return BunnyCDN connector results as JSON when actions are executed with --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
