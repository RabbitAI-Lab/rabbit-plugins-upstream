## Description:

Helps agents diagnose and recover Chocolatey upgrade issues involving NSSM service paths, NSSM-to-shawl migrations, and stale Chocolatey metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and Windows administrators use this skill to plan and review Chocolatey package maintenance, NSSM service path refreshes, service migration to shawl, and metadata resynchronization after upgrades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend broad administrator-level Chocolatey package or Windows service changes.

Mitigation: Review each package and service name before execution, prefer targeted commands, and avoid choco upgrade all -y unless broad system changes are intended.

Risk: Service path refreshes or NSSM-to-shawl migrations can stop, remove, or misconfigure Windows services.

Mitigation: Record existing service configuration before changes and verify service account, path, status, and application behavior after each change.

Risk: The shawl migration workflow may involve downloading an executable and handling Windows service credentials.

Mitigation: Verify any downloaded shawl binary and avoid saving plaintext Windows passwords in scripts or logs.

## Reference(s):

- [Chocolatey documentation](https://docs.chocolatey.org/)
- [UniGetUI repository](https://github.com/Devolutions/UniGetUI)
- [chocolatey/choco repository](https://github.com/chocolatey/choco)
- [shawl repository](https://github.com/mtkennerly/shawl)
- [Syncthing v2.0 release notes](https://github.com/syncthing/syncthing/releases/tag/v2.0.0)
- [Syncthing issue 10340](https://github.com/syncthing/syncthing/issues/10340)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline Bash, PowerShell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include administrator-level commands for Windows package and service maintenance]

## Skill Version(s):

1.0.5 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
