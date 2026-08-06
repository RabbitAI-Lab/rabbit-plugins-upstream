## Description:

Provides Chocolatey operations guidance for post-upgrade checks, NSSM service path refresh, NSSM-to-shawl migration, and UniGetUI or Chocolatey metadata update recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and Windows operators use this skill to diagnose and repair Chocolatey upgrade side effects, especially stale NSSM service paths, NSSM-to-shawl migration cases, and stale Chocolatey package metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrator-level Chocolatey and Windows service commands can make broad system changes.

Mitigation: Confirm the package or service name and intended admin scope before running generated commands.

Risk: Bulk upgrades and service stop/start operations can disrupt running workloads.

Mitigation: Use a maintenance window, and avoid `choco upgrade all -y` unless a system-wide upgrade is intended.

Risk: Service migration guidance may involve Windows account credentials.

Mitigation: Use prompted or secure credential handling, and do not paste or store Windows passwords in scripts or chat logs.

## Reference(s):

- [Chocolatey Documentation](https://docs.chocolatey.org/)
- [UniGetUI Repository](https://github.com/Devolutions/UniGetUI)
- [shawl Repository](https://github.com/mtkennerly/shawl)
- [Chocolatey CLI Repository](https://github.com/chocolatey/choco)
- [Syncthing issue 10340](https://github.com/syncthing/syncthing/issues/10340)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell, PowerShell, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated administrator commands and diagnostic JSON for Windows service operations.]

## Skill Version(s):

1.0.2 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
