## Description:

Chocolatey operations integration for post-processing after Chocolatey upgrades, refreshing NSSM service paths, migrating NSSM services to shawl, and recovering stale UniGetUI or Chocolatey metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and Windows administrators use this skill to diagnose Chocolatey-managed NSSM services after package upgrades, generate service path refresh commands, migrate affected services to shawl, and reconcile stale Chocolatey metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Windows service and package-management commands may disrupt production services if run without preparation.

Mitigation: Review the exact package and service names, back up current NSSM or service configuration, and perform service removal or upgrade operations during a maintenance window.

Risk: The shawl migration workflow downloads and installs a service wrapper binary.

Mitigation: Verify the downloaded shawl binary before use and keep the installation path explicit.

Risk: Service account or credential changes can break access to user data or expose passwords.

Mitigation: Preserve the existing service account where appropriate, avoid hardcoding plaintext passwords, and prompt for or otherwise protect credentials.

Risk: Broad Chocolatey upgrades can update many packages and trigger unexpected service changes.

Mitigation: Prefer targeted upgrades when possible, verify Chocolatey metadata after changes, and confirm affected service status before and after the operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/choco)
- [Chocolatey documentation](https://docs.chocolatey.org/)
- [UniGetUI repository](https://github.com/Devolutions/UniGetUI)
- [shawl repository](https://github.com/mtkennerly/shawl)
- [chocolatey/choco repository](https://github.com/chocolatey/choco)
- [Syncthing v2.0 release notes](https://github.com/syncthing/syncthing/releases/tag/v2.0.0)
- [Syncthing issue 10340](https://github.com/syncthing/syncthing/issues/10340)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, PowerShell, and JSON command output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes diagnostic summaries, service path analysis, and administrator command sequences for Windows service maintenance.]

## Skill Version(s):

1.0.4 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
