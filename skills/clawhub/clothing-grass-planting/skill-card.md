## Description:

Generates social-commerce clothing seeding image guidance by preserving an outfit while changing the model, pose, scene, lighting, and camera style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agents use this skill to create lifestyle social-commerce clothing images from outfit photos. It guides prompt writing and command execution while keeping garment details stable and varying the model, scene, pose, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images may be sent to the selected image provider.

Mitigation: Use trusted local files or public image URLs, avoid private or internal URLs, and submit only images the user owns or is authorized to edit.

Risk: Lifestyle clothing images can be misused to imply a real person's endorsement or product experience.

Mitigation: Do not generate specific-person face swaps, forged endorsements, or fake user-experience imagery.

Risk: Low-quality or obstructed source images can cause garment details to be redrawn incorrectly.

Mitigation: Use clear single-subject outfit images above the documented size and resolution thresholds, and explicitly name each garment, accessory, color, pattern, texture, and fit in the prompt.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI](https://github.com/dlazyai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, bash command examples, and optional JSON status envelopes from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, the workflow typically saves JPEG image files, with the clothing-grass-planting task defaulting to 1024x1536 at medium quality.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
