## Description:

Guides ecommerce image-editing workflows that replace a model, a background, or both while keeping the product unchanged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and creative operators use this skill to create audience- and scene-specific model-photo variants from an existing product photo while preserving the garment. Agents use it to choose the edit mode, prepare prompts, check input constraints, and generate provider commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the selected cloud image provider.

Mitigation: Use only images the user is authorized to upload; choose the provider explicitly and use dry-run in sensitive workflows.

Risk: Model or face references can create likeness or endorsement concerns.

Mitigation: Use authorized product, model, and face images only; avoid non-consensual likenesses or fabricated endorsements.

Risk: Generated edits may alter product details, fit, lighting, or anatomy.

Mitigation: Review outputs against the product invariants, alignment, hand structure, and lighting before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/one-shot)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline bash commands and generated image file paths or JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save JPEG, PNG, or WebP image files through configured cloud image providers.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
