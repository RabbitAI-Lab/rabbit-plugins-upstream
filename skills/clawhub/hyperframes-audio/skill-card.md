## Description:

Helps agents mix already placed audio in a HyperFrames composition by authoring fades, track volume and gain, automation, ducking, voiceover carve, and track effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to adjust audio that is already placed in HyperFrames compositions, including voice/music balance, effect chains, automation envelopes, and command-line voiceover carve operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The carve script can overwrite or duplicate existing mix data when HyperFrames audio attributes are hand-edited or single-quoted.

Mitigation: Use version control or a backup, run `scripts/carve.mjs` with `--dry-run` first, and normalize existing data-fx-chain, data-automation, and data-fx-carve attributes to double-quoted HTML before allowing writes.

## Reference(s):

- [Audio attributes](references/attributes.md)
- [Diagnosing audio you cannot hear](references/diagnosis.md)
- [Effect registry](references/fx-registry.md)
- [Presets, jobs and one-knob profiles](references/presets.md)
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-audio)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply HyperFrames audio attribute changes; the carve script should be dry-run before writes when existing mix attributes may be hand-edited.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
