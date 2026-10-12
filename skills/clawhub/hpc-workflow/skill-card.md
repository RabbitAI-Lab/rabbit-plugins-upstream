## Description:

Sets up, adapts, and recovers agent-operated Slurm GPU workspaces with persistent tmux sessions, durable allocation requests, job-local storage, and verified automatic backups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[playeriv65](https://clawhub.ai/user/playeriv65)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and HPC operators use this skill to configure an authorized Slurm GPU workspace, operate persistent jobs and backups, and recover from interrupted connections or deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on cloning and running an unpinned external repository.

Mitigation: Review the matching repository revision and helper scripts, then pin or verify the commit before use.

Risk: Agent access to an authenticated HPC environment could expose credentials or private site configuration.

Mitigation: Grant only authorized access, keep private profiles out of public repositories, and require approval for credential prompts.

Risk: Automatic cancellation, deletion, or recovery could interrupt jobs or destroy research data.

Mitigation: Require explicit approval for destructive actions and preserve uncertain job records and backups.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/playeriv65/skills/hpc-workflow)
- [Project repository (metadata link; review matching revision)](https://github.com/playeriv65/hpc-agent-kit)
- [Site probing](references/site-probing.md)
- [Acceptance evidence](references/acceptance.md)
- [Operating lessons](references/operations.md)
- [Recovery and upgrades](references/recovery.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and site-profile instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Site-specific operating notes and verification limits; no fixed machine-readable output.]

## Skill Version(s):

0.4.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
