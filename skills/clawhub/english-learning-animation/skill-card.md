## Description:

Create short, character-led English-learning videos with layered editorial-cartoon visuals, role-matched Qwen3-TTS voices, English-only on-video copy, and audio-driven timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT

## Use Case:

External creators, educators, and developers use this skill to produce short English-learning animation videos with scripted dialogue, role-specific synthetic voices, layered visuals, and preflight and post-render quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python, ffmpeg/ffprobe, Remotion/Node tooling, and a local Qwen3-TTS checkpoint.

Mitigation: Run it in a new or empty project directory, review command arguments and paths before execution, and keep model and output paths away from sensitive locations.

Risk: Generated English-learning videos can contain mismatched scenes, stale phrase cards, timing errors, or misleading visual emphasis that mechanical checks cannot fully judge.

Mitigation: Run the bundled preflight and post-render validators, then inspect the cover and one extracted review frame per spoken segment before publishing.

Risk: Generated voices, images, and final videos may carry publication or licensing obligations outside the skill package.

Mitigation: Confirm rights for the local Qwen3-TTS checkpoint, generated visual assets, audio, and final rendered video before distribution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tobewin/skills/english-learning-animation)
- [Source Repository](https://github.com/ToBeWin/english-learning-animation)
- [Quality Gates](references/quality-gates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and shell command snippets, plus project files and JSON configuration templates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local animation project scaffolding, voice manifests, validation commands, and review-frame guidance; generated model weights, voices, and final videos are not bundled.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
