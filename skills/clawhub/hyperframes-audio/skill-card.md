## Description:

Helps creators mix audio already placed in a HyperFrames composition with fades, automation, effects, submix buses, and voiceover carving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to balance music, voice, and effects in existing HyperFrames compositions, including automating levels and carving space for narration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio-mixing commands can change composition HTML attributes.

Mitigation: Review the selected composition and proposed track changes; use dry-run before writing when appropriate.

Risk: Unpinned project tooling may change behavior between runs.

Mitigation: Prefer project-local, lockfile-backed HyperFrames tooling or pinned npx versions.

## Reference(s):

- [HyperFrames Audio on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [Audio attributes](artifact/references/attributes.md)
- [Effect registry](artifact/references/fx-registry.md)
- [Audio diagnosis](artifact/references/diagnosis.md)
- [Mixing presets](artifact/references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance and HTML audio attributes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update a specified composition HTML file; does not source or generate audio.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
