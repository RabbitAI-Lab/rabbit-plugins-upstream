## Description:

Covers macOS app development with Swift 6.3, SwiftUI, SwiftData, Swift Concurrency, Foundation Models, Swift Testing, ScreenCaptureKit, and app distribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill when building native macOS apps with Swift, including SwiftUI interfaces, SwiftData persistence, concurrency, on-device AI, capture workflows, testing, distribution, and system integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documents privacy-sensitive macOS APIs for recording, process monitoring, login items, daemons, and background apps.

Mitigation: Use those patterns only with explicit user consent, visible controls, appropriate macOS privacy permissions, and clear disable or uninstall paths.

Risk: Installer and toolchain setup snippets can execute remote content or modify local developer environments.

Mitigation: Verify source URLs and script contents before running remote installer commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/swift-macos)
- [Homepage](https://github.com/tenequm/skills/tree/main/skills/swift-macos)
- [App Lifecycle & Scenes](references/app-lifecycle.md)
- [macOS-Specific SwiftUI](references/swiftui-macos.md)
- [AppKit Interop](references/appkit-interop.md)
- [Screen Capture & Audio Recording](references/screen-capture-audio.md)
- [CoreAudio Process Tap (CATap)](references/core-audio-tap.md)
- [System Integration](references/system-integration.md)
- [Foundation Models Framework](references/foundation-models.md)
- [Architecture Patterns for macOS Apps](references/architecture.md)
- [Testing macOS Apps](references/testing.md)
- [macOS App Distribution](references/distribution.md)
- [Swift Package Manager & Build](references/spm-build.md)
- [Approachable Concurrency (Swift 6.2)](references/approachable-concurrency.md)
- [Actors & Isolation](references/actors-isolation.md)
- [Structured Concurrency](references/structured-concurrency.md)
- [Sendable & Data Race Safety](references/sendable-safety.md)
- [Async Patterns](references/async-patterns.md)
- [Concurrency Migration Guide](references/migration-guide.md)
- [Models & Schema](references/models-schema.md)
- [Relationships & Predicates](references/relationships-predicates.md)
- [ModelContainer & ModelContext](references/container-context.md)
- [CloudKit Sync](references/cloudkit-sync.md)
- [Schema Migrations](references/migrations.md)
- [Fall 2026 Releases (WWDC 2026)](references/fall-2026-releases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Swift and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces advisory development guidance and examples; it does not install or run code by itself.]

## Skill Version(s):

0.7.1 (source: frontmatter and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
