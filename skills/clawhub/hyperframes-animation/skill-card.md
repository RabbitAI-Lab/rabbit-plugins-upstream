## Description:

Provides HyperFrames animation guidance across atomic motion rules, scene blueprints, transitions, design techniques, runtime adapters, and animation-map auditing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion authors use this skill to select and combine HyperFrames animation rules, blueprints, transitions, runtime adapters, and audit tools for deterministic, seek-safe composition work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples or generated compositions may fetch animation libraries from public CDNs.

Mitigation: For production use, vendor or pin remote libraries and apply integrity controls before running or shipping the composition.

Risk: The animation-map script can fall back to an unpinned package version when used outside a bundled install.

Mitigation: Set HYPERFRAMES_SKILL_PKG_VERSION when running the script outside the bundled CLI or skill installation.

Risk: Glitch, flash, and high-brightness effects can create accessibility and photosensitivity concerns.

Mitigation: Provide reduced-motion and photosensitivity-safe alternatives before shipping these effects.

## Reference(s):

- [HyperFrames Animation Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Rules Index](artifact/rules-index.md)
- [Blueprints Index](artifact/blueprints-index.md)
- [Scene Transitions Overview](artifact/transitions/overview.md)
- [Visual Techniques Reference](artifact/techniques.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Analysis]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HyperFrames-native guidance emphasizes deterministic, seek-safe animation timelines.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
