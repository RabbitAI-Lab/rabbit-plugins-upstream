## Description:

Guides agents building, debugging, and releasing WPF desktop apps on .NET, including tray behavior, single-file publishing, DPI, startup performance, and release CI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rockbenben](https://clawhub.ai/user/rockbenben)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan WPF project setup, diagnose desktop UI and startup issues, add smoke and screenshot checks, and prepare GitHub Actions release workflows for Windows desktop apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reference files are primarily Chinese, which can lead to misunderstood implementation or release guidance.

Mitigation: Use the skill only when the reader can review the Chinese documentation accurately or translate it before applying changes.

Risk: Release workflow guidance touches GitHub permissions, OIDC attestations, and WINGET_TOKEN scope.

Mitigation: Verify current action versions, release permissions, attestation permissions, and token scope before using the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rockbenben/skills/wpf-desktop)
- [project-setup.md](project-setup.md)
- [pitfalls.md](pitfalls.md)
- [dev-switches.md](dev-switches.md)
- [github-actions.md](github-actions.md)
- [.NET and .NET Core support policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-core)
- [WPF localization documentation](https://learn.microsoft.com/dotnet/desktop/wpf/advanced/how-to-localize-an-application)
- [SDK, MSBuild, and Visual Studio versioning](https://learn.microsoft.com/dotnet/core/porting/versioning-sdk-msbuild-vs)
- [H.NotifyIcon.Wpf package](https://www.nuget.org/packages/H.NotifyIcon.Wpf)
- [GitHub artifact attestations action](https://github.com/actions/attest)
- [winget-create](https://github.com/microsoft/winget-create)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline C#, XAML, YAML, PowerShell, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows WPF guidance; referenced documentation files are primarily Chinese.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
