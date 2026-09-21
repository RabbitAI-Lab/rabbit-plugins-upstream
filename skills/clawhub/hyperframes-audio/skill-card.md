## Description:

HyperFrames Audio helps agents mix existing audio in HyperFrames compositions with fades, crossfades, gain and volume automation, ducking, voiceover carve, effect chains, and submix bus guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to finish audio mixes in HyperFrames compositions after media has already been placed. It supports choosing and writing audio attributes for track effects, automation, ducking, voiceover carve, and reusable group-level processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the carve workflow can modify declared audio attributes in a HyperFrames composition.

Mitigation: Run the carve script with --dry-run first and keep the composition under version control before writing changes.

Risk: Following npx or npm examples may execute HyperFrames tooling from the local project or package registry.

Mitigation: Use the skill only in projects where the HyperFrames toolchain is trusted, and prefer pinned or already-installed CLI/core versions.

Risk: Audio diagnosis can be ambiguous when there is no clean original, usable silence, or listener-provided symptom.

Mitigation: Report the ambiguity and ask for a listening judgment instead of inventing a confident correction.

## Reference(s):

- [The three audio attributes](references/attributes.md)
- [Diagnosing audio you cannot hear](references/diagnosis.md)
- [Effect registry](references/fx-registry.md)
- [Presets, jobs and one-knob profiles](references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HyperFrames audio attribute JSON for data-fx-chain, data-automation, and data-fx-carve.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
