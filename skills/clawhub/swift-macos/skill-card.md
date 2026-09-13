## Description:

macOS apps with Swift 6.3, SwiftUI, SwiftData, Swift Concurrency, Foundation Models, Swift Testing, and ScreenCaptureKit. Use when building native Mac apps - windows, menus, SwiftData, on-device AI, capture, AppKit bridges, notarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill for guidance when building native macOS applications with SwiftUI, SwiftData, Swift Concurrency, Foundation Models, ScreenCaptureKit, testing, signing, notarization, and distribution workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested shell commands may include a remote installer command.

Mitigation: Verify the installer source separately before running any curl-to-bash command, and prefer reviewed or pinned installation steps.

Risk: Screen and audio capture examples can affect user privacy when copied into applications.

Mitigation: Require explicit user consent, use the narrowest capture scope, and provide a visible recording state before using capture recipes.

Risk: Signing and notarization examples involve credentials or signing keys.

Mitigation: Use keychain-backed credentials, avoid embedding secrets, and review key handling before executing distribution commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/swift-macos)
- [Project homepage from ClawHub metadata](https://github.com/tenequm/skills/tree/main/skills/swift-macos)
- [Fall 2026 Releases](references/fall-2026-releases.md)
- [App Lifecycle & Scenes](references/app-lifecycle.md)
- [macOS-Specific SwiftUI](references/swiftui-macos.md)
- [AppKit Interop](references/appkit-interop.md)
- [Screen Capture & Audio Recording](references/screen-capture-audio.md)
- [CoreAudio Process Tap](references/core-audio-tap.md)
- [System Integration](references/system-integration.md)
- [Foundation Models](references/foundation-models.md)
- [Architecture Patterns for macOS Apps](references/architecture.md)
- [Testing macOS Apps](references/testing.md)
- [Distribution](references/distribution.md)
- [Swift Package Manager & Build](references/spm-build.md)
- [Approachable Concurrency](references/approachable-concurrency.md)
- [Actors & Isolation](references/actors-isolation.md)
- [Structured Concurrency](references/structured-concurrency.md)
- [Sendable & Data Race Safety](references/sendable-safety.md)
- [Async Patterns](references/async-patterns.md)
- [Migration Guide](references/migration-guide.md)
- [Models & Schema](references/models-schema.md)
- [Relationships & Predicates](references/relationships-predicates.md)
- [ModelContainer & ModelContext](references/container-context.md)
- [CloudKit Sync](references/cloudkit-sync.md)
- [SwiftData Migrations](references/migrations.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Swift and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include macOS-version-specific API gates, build commands, entitlements, permissions guidance, and signing or notarization examples.]

## Skill Version(s):

0.8.3 (source: frontmatter, changelog, and server release metadata; released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
