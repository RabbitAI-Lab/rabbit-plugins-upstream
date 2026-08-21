## Description:

Covers macOS app development with Swift 6.3, SwiftUI, SwiftData, Swift Concurrency, Foundation Models, Swift Testing, ScreenCaptureKit, and app distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill as a macOS development reference when building native Swift apps that involve SwiftUI, SwiftData, concurrency, system integration, screen and audio capture, testing, and distribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples cover sensitive macOS capabilities including CloudKit sync, Accessibility, screen and audio capture, login items, and daemons.

Mitigation: Review permissions, user consent, signing, sandboxing, and data-handling requirements before applying those examples in an app.

Risk: Distribution and setup guidance may include Gatekeeper overrides or remote install commands.

Mitigation: Verify provenance, prefer notarized and signed installers, and inspect remote scripts before execution.

Risk: The documentation targets specific Swift, Xcode, and macOS versions, so examples can become stale or version-gated.

Mitigation: Check examples against the target SDK and deployment version before shipping generated code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/swift-macos)
- [Clawdis homepage](https://github.com/tenequm/skills/tree/main/skills/swift-macos)
- [App Lifecycle & Scenes](references/app-lifecycle.md)
- [macOS-Specific SwiftUI](references/swiftui-macos.md)
- [ModelContainer & ModelContext](references/container-context.md)
- [Relationships & Predicates](references/relationships-predicates.md)
- [Schema Migrations](references/migrations.md)
- [Approachable Concurrency (Swift 6.2)](references/approachable-concurrency.md)
- [Structured Concurrency](references/structured-concurrency.md)
- [Sendable & Data Race Safety](references/sendable-safety.md)
- [Foundation Models Framework](references/foundation-models.md)
- [Screen Capture & Audio Recording](references/screen-capture-audio.md)
- [System Integration](references/system-integration.md)
- [macOS App Distribution](references/distribution.md)
- [Testing macOS Apps](references/testing.md)
- [Swift Package Manager & Build](references/spm-build.md)
- [Fall 2026 Releases (WWDC 2026)](references/fall-2026-releases.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with Swift and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance for agent responses; examples should be reviewed against the target macOS, Swift, and Xcode versions before use.]

## Skill Version(s):

0.8.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
