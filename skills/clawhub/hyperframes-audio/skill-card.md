## Description:

Helps agents mix audio already placed in a HyperFrames composition by applying voiceover carve settings, track effects, and automation envelopes while avoiding unrelated audio sourcing, generation, timing, or layout work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to adjust audio mixes in HyperFrames HTML compositions, especially to make music beds leave room for voiceover and to express effect chains or automation as composition attributes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI can rewrite the selected HyperFrames HTML composition when not run in dry-run mode.

Mitigation: Review the target composition, run the helper with --dry-run first, and keep the file under backup or version control before allowing writes.

Risk: Audio diagnosis without a clean original or usable pauses can be under-determined and may lead to overconfident corrective chains.

Mitigation: Report ambiguous measurements, ask for a human listening judgment when needed, and prefer documented presets or measured comparisons over unsupported fixes.

## Reference(s):

- [Skill page](https://clawhub.ai/heygen-com/skills/hyperframes-audio)
- [The three audio attributes](references/attributes.md)
- [Diagnosing audio you cannot hear](references/diagnosis.md)
- [Effect registry](references/fx-registry.md)
- [Presets, jobs and one-knob profiles](references/presets.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline JSON attributes, code snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run a bundled Node.js helper that rewrites a selected HyperFrames HTML composition unless dry-run mode is used.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
