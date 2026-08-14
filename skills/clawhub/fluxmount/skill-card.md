## Description:

FluxMount helps macOS users make external NTFS drives writable by guiding installation, verification, automation, and rollback of macFUSE and ntfs-3g based mounting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hackerfish](https://clawhub.ai/user/hackerfish)

### License/Terms of Use:

MIT

## Use Case:

External macOS users, desktop-agent users, and support engineers use this skill when an external NTFS drive mounts read-only and they need commands, bundled scripts, and guidance to install, verify, automate, or roll back read-write mounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports privileged disk-mounting automation with passwordless sudo and startup or hot-plug persistence enabled by default.

Mitigation: Review the scripts before use, run dry-run first, and disable or edit the sudoers and LaunchAgent automation unless unattended remounting is explicitly desired.

Risk: Disk mounting changes can affect external-drive access if run on the wrong system or without preparation.

Mitigation: Install only on a trusted Mac, back up important external-drive data first, and use the provided uninstall path to remove FluxMount changes.

Risk: The workflow installs macFUSE and ntfs-3g dependencies, including download paths that may use mirrors.

Mitigation: Prefer official sources where possible and verify the macFUSE package signer or checksum before installation.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/hackerFish/fluxmount)
- [ClawHub skill page](https://clawhub.ai/hackerfish/skills/fluxmount)
- [macFUSE](https://github.com/macfuse/macfuse)
- [ntfs-3g](https://github.com/tuxera/ntfs-3g)
- [Troubleshooting guide](references/troubleshooting.md)
- [Safety and rollback notes](SAFETY.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command blocks and bundled shell scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local macOS terminal guidance and script-driven install, doctor, status, dry-run, automount, and uninstall workflows.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and manifest state 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
