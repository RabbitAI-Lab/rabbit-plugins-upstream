## Description:

Guides developers in configuring and running multiple persistent forward and reverse SSH tunnels across hosts from a single rules file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up and maintain concurrent SSH tunnels for reaching remote services or exposing local services to trusted remote hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested installer pipes a mutable remote script directly into bash without integrity verification.

Mitigation: Download a pinned release or source checkout, inspect it, and verify integrity before execution; avoid the pipe-to-bash installer.

Risk: Reverse tunnels can expose local services to remote hosts.

Mitigation: Review tunnel rules and remote hosts before use, and expose only services intended for those hosts.

Risk: SSH private keys and rules files contain sensitive access information.

Mitigation: Keep keys and rules files private, and prefer a current-user installation unless system-wide access is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/ssh-tunnel-swarm)
- [Setup and configuration reference](references/setup.md)
- [Project homepage listed by the skill](https://github.com/psyb0t/ssh-tunnel-swarm)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and rules-file examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses environment variables and a rules file; no CLI flags.]

## Skill Version(s):

1.4.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
