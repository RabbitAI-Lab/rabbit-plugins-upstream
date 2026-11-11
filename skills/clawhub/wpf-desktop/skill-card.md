## Description:

Helps developers build, maintain, fix, or assess Windows WPF apps, with guidance on .NET 10 upgrades, XAML, DPI, tray behavior, dependencies, and releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining Windows desktop software use this skill to build, upgrade, troubleshoot, and assess WPF applications, including their UI behavior, dependencies, and release workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cleanup guidance could remove files used by another application.

Mitigation: Before following cleanup steps, confirm each target path is owned by the WPF application and preserve user data.

Risk: Some referenced material was only partially inspected, so the scan does not establish that all content is safe.

Mitigation: Review the cleanup guidance and any partially inspected material before installing or acting on it.

## Reference(s):

- [Project setup and publishing](artifact/project-setup.md)
- [Dependency upgrades](artifact/upgrade-dependencies.md)
- [WPF troubleshooting guide](artifact/pitfalls.md)
- [Validation coverage](artifact/VALIDATION.md)
- [Microsoft .NET SDK selection](https://learn.microsoft.com/dotnet/core/tools/global-json)
- [Microsoft NuGet central package management](https://learn.microsoft.com/nuget/consume-packages/central-package-management)
- [Release workflow reference](https://github.com/rockbenben/aishort-skills/blob/main/skills/desktop-app-standard/references/release-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-specific recommendations and verification steps; examples may include C#, XAML, XML, JSON, PowerShell, and GitHub Actions configuration.]

## Skill Version(s):

1.3.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
