## Description:

Bring existing video code or footage into HyperFrames and verify it frame by frame against the original - Remotion first, also Motion Canvas, Lottie, Three.js, p5.js, canvas or plain HTML/CSS animation, or renders from Manim, After Effects or Blender. Use to port, convert, migrate or reuse work made with another tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to bring existing Remotion and other animation or video projects into HyperFrames, choosing a native translation, hosted runtime, or rendered media based on source capabilities. It guides frame-by-frame comparison against the source and recording of translation differences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned commands and dependencies may download and run changing third-party code.

Mitigation: Verify package versions and review external requests and execution steps before installation; if proceeding, use a restricted environment without sensitive files or credentials.

Risk: The security scan was partial: 70 of 72 components were scanned, some references could not be resolved, and one static analyzer was degraded.

Mitigation: Treat the scan as incomplete and review the unresolved references and execution steps before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/remotion-to-hyperframes)
- [API mapping](artifact/references/api-map.md)
- [Escape hatch for unsupported Remotion features](artifact/references/escape-hatch.md)
- [Translation limitations](artifact/references/limitations.md)
- [Frame comparison and evaluation](artifact/references/eval.md)
- [Runtime interop implementation (PR #214)](https://github.com/heygen-com/hyperframes/pull/214)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and translated HTML/CSS/GSAP project code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Translation may be lossy; the skill calls for frame-by-frame comparison and notes on differences.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
