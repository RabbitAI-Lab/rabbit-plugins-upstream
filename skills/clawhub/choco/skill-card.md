## Description:

Chocolatey operations integration for post-processing after choco upgrades, refreshing NSSM service paths, migrating NSSM-managed services to shawl, and recovering UniGetUI or Chocolatey metadata update failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and system administrators use this skill to diagnose Chocolatey and NSSM service issues after Windows package upgrades, generate repair commands, and apply guided migration or metadata recovery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can suggest administrator-level Chocolatey and Windows service operations that may disrupt services if applied broadly or without review.

Mitigation: Apply commands only to specific packages or services you have identified, review pending Chocolatey changes first, and avoid bulk upgrade operations unless service disruption is acceptable.

Risk: Migrating NSSM services to shawl can change the Windows service execution account or lose existing service settings.

Mitigation: Export or record the existing service configuration, especially ObjectName, paths, arguments, and log settings, before re-registering the service.

Risk: The shawl workflow may require downloading a Windows binary outside the package manager path.

Mitigation: Verify downloaded shawl binaries independently before installing or using them.

## Reference(s):

- [Choco Skill on ClawHub](https://clawhub.ai/drumrobot/skills/choco)
- [Publisher Profile](https://clawhub.ai/user/drumrobot)
- [Chocolatey Documentation](https://docs.chocolatey.org/)
- [UniGetUI Repository](https://github.com/Devolutions/UniGetUI)
- [shawl Repository](https://github.com/mtkennerly/shawl)
- [chocolatey/choco Repository](https://github.com/chocolatey/choco)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline shell, PowerShell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose administrator-level Windows service and Chocolatey commands that require user review before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
