## Description:

Provides guidance and examples for building native macOS apps with Swift, SwiftUI, SwiftData, concurrency, on-device AI, and screen capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, implement, test, and distribute native macOS apps, including SwiftUI interfaces, SwiftData persistence, system integration, and media capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested remote installation, signing or keychain, and privacy-permission reset commands can change the developer's system or credentials.

Mitigation: Review each command and its source before execution; use test credentials and avoid resetting permissions unnecessarily.

Risk: Apps built from screen, audio, microphone, accessibility, or CloudKit examples may handle sensitive information.

Mitigation: Request only necessary permissions, disclose capture and sync behavior, and test privacy controls before release.

Risk: Login-item and daemon examples could introduce unwanted background behavior in an app.

Mitigation: Include background components only when needed and make their activation and removal clear to users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tenequm/skills/swift-macos)
- [Project homepage listed in skill metadata](https://github.com/tenequm/skills/tree/main/skills/swift-macos)
- [Screen capture and audio reference](references/screen-capture-audio.md)
- [Distribution reference](references/distribution.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Text or Markdown with Swift and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples require review and adaptation to the target macOS version and app permissions.]

## Skill Version(s):

0.8.5 (source: skill metadata, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
