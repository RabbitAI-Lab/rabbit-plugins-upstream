## Description:

Generates Chinese, plugin-importable JSON presets for Nano Banana/Gemini cosplay photo edits, including visual effects, retouching, style recognition, and reverse prompt reconstruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aleaaaan](https://clawhub.ai/user/aleaaaan)

### License/Terms of Use:

MIT

## Use Case:

External users, cosplay creators, and image-editing agents use this skill to turn natural-language COS photo editing requests into structured JSON presets for Nano Banana/Gemini image editing. It also supports image-effect reverse analysis and style preset generation when the active agent can inspect images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save generated JSON preset files into the user's Downloads folder.

Mitigation: Review the output path and generated JSON before importing or sharing the preset.

Risk: Confirmed new style entries can be persisted into the skill's learned-style reference file.

Mitigation: Review learned style entries before accepting them, and only add styles that are relevant to COS photo editing.

Risk: Using the skill for unrelated general style discussion can produce outputs outside the disclosed COS photo preset workflow.

Mitigation: Use the skill for COS photo editing presets, reverse effect analysis, and closely related style preset tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/aleaaaan/skills/cos-effect-prompt-main)
- [README](README.md)
- [COS Effects Reference](references/effects.md)
- [Preset Envelope Example](references/preset-envelope.json)
- [Instruction Template](references/template.json)
- [Portrait Processing Reference](references/portrait.md)
- [Fallback Module Reference](references/fallback.md)
- [MJ Style Reference](references/mj-style.md)
- [Nano Banana Prompting Notes](references/nano-banana.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown with JSON code blocks and plugin-importable JSON preset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preset envelopes include id, title, serialized content, slider params, category, subCategory, refImages, and _isFactory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
