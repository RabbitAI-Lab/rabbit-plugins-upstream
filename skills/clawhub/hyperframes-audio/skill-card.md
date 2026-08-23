## Description:

Supports HyperFrames audio mixing for placed audio and video tracks, including fades, crossfades, track gain, volume and effect automation, ducking, voiceover carve, and audio effect chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content engineers use this skill to modify audio-mixing attributes in HyperFrames compositions and to produce guidance for diagnosing, carving, automating, and effect-processing placed audio. It is not intended for sourcing, generating, or retiming media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve CLI can rewrite data-fx-carve, data-fx-chain, and data-automation attributes on a HyperFrames composition file.

Mitigation: Run --dry-run first, review the selected bed and voice tracks plus generated attributes, and keep version-control or backup protection before running without --dry-run.

Risk: Incorrect bed, voice, or group selection can produce an audio mix that ducks or carves the wrong material.

Mitigation: Use explicit --bed and --voice arguments or a voice-only data-audio-group when automatic selection is uncertain, then render and listen to verify the mix.

## Reference(s):

- [HyperFrames Audio Skill Source](artifact/SKILL.md)
- [The three audio attributes](artifact/references/attributes.md)
- [Diagnosing audio you cannot hear](artifact/references/diagnosis.md)
- [Effect registry](artifact/references/fx-registry.md)
- [Presets, jobs and one-knob profiles](artifact/references/presets.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-audio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON attribute examples and optional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit commands for scripts/carve.mjs; --dry-run reports proposed changes without writing.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
