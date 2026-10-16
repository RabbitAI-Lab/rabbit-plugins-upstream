## Description:

Helps agents inspect and manage ZeroTier networks, members, and organization resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and administrators use this skill to inspect ZeroTier networks and members and manage connected networks, access, and organization resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested CLI setup executes a remote installation script without verification.

Mitigation: Review the installation source and prefer official, version-pinned instructions with checksum or signature verification.

Risk: Destructive actions can revoke access or permanently remove ZeroTier resources.

Mitigation: Use an account with only the required permissions and confirm the exact targets and effects before changes.

## Reference(s):

- [ZeroTier skill on ClawHub](https://clawhub.ai/oomol/skills/oo-zerotier)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ZeroTier](https://www.zerotier.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, JSON responses, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected account and its permissions.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
