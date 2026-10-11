## Description:

Provides guidance and examples for building native macOS apps with Swift, SwiftUI, SwiftData, concurrency, on-device AI, testing, and ScreenCaptureKit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill for guidance and code examples when building, testing, and distributing native macOS applications, including data persistence, screen and audio capture, and system integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Development examples include sensitive shell commands for installation, signing, keychain access, TCC resets, and persistent system components.

Mitigation: Review commands and their effects before running them; do not execute examples automatically.

Risk: Screen, audio, microphone, accessibility, and persistence features can access sensitive user data.

Mitigation: Request clear user consent and appropriate system permissions before enabling those features.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/swift-macos)
- [Homepage listed in skill metadata](https://github.com/tenequm/skills/tree/main/skills/swift-macos)
- [SwiftUI for macOS](artifact/references/swiftui-macos.md)
- [SwiftData models and schemas](artifact/references/models-schema.md)
- [Screen capture and audio](artifact/references/screen-capture-audio.md)
- [App distribution](artifact/references/distribution.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Swift and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples are guidance, not automatically executed.]

## Skill Version(s):

0.8.4 (source: release metadata, skill frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
