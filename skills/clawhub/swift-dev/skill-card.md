## Description:

Provides Swift development guidance for native iOS and macOS apps, including SwiftUI, SwiftData, concurrency, testing, signing, and distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill as a reference when building, testing, signing, and distributing native iPhone and Mac apps in Swift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signing, App Store Connect, and notarization steps may expose privileged credentials.

Mitigation: Use credentials only for the intended account and project, and review each command before running it.

Risk: Xcode MCP always-allow settings and macOS Accessibility, login-item, screen, or audio permissions may grant sensitive access.

Mitigation: Enable only the access needed for the specific project and verify the permission request before approving it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tenequm/skills/swift-dev)
- [Publisher-provided skill homepage](https://github.com/tenequm/skills/tree/main/skills/swift-dev)
- [iOS project setup reference](references/ios-project-setup.md)
- [Swift concurrency reference](references/concurrency-isolation.md)
- [macOS distribution reference](references/macos-distribution.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Swift, shell, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference guidance; project-specific commands and permissions require review.]

## Skill Version(s):

0.2.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
