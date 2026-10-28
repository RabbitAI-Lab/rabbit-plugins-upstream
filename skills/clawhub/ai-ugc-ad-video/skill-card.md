## Description:

Creates labeled vertical AI UGC product ads by guiding creator casting, scripting, shot-by-shot generation, review, and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketers and creative teams use this skill to plan and create labeled AI UGC ads for products, including creator concepts, scripts, video prompts, review checks, and edit guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos or recordings may include content the user lacks permission to share with the generation service.

Mitigation: Use only photos and recordings you have permission to share with varg and its generation providers.

Risk: Confidential assets or API credentials could be exposed.

Mitigation: Avoid confidential assets and protect the VARG_API_KEY.

Risk: Video generation can spend credits, including on retakes.

Mitigation: Review the full credit estimate before approving generation.

## Reference(s):

- [Prompt templates](references/prompts.md)
- [Varg: Make a UGC ad video](https://varg.ai/how-to/make-a-ugc-ad-video)
- [BytePlus Seedance 2.5 prompt guide](https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5-prompt-guide)

## Skill Output:

**Output Type(s):** [Video, Text, JSON prompts]

**Output Format:** [Vertical MP4 video with reusable text and JSON generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 9:16 at 1080×1920; output and generation time vary by selected format and service.]

## Skill Version(s):

1.0.0 (source: frontmatter; ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
