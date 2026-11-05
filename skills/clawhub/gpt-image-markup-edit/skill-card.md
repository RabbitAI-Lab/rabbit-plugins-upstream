## Description:

Markup-guided image edits with GPT Image 2.6 on Varg let users target specific regions with colored annotations and ask the model to preserve the rest of the image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image creators use this skill to specify localized image changes with colored markup, then submit an edit prompt that asks the model to preserve unmarked areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and annotations are uploaded to Varg and downstream processing providers.

Mitigation: Only upload images you are comfortable sharing, and check the providers’ privacy and retention terms before sending confidential material.

Risk: An image edit may change areas outside the annotations.

Mitigation: Keep the original and review the result with a visual comparison before using it.

Risk: Image processing consumes credits.

Mitigation: Consider the credit cost before submitting an edit.

## Reference(s):

- [Varg how-to](https://varg.ai/how-to)
- [Varg MCP connection](https://mcp.varg.ai/mcp)
- [OpenAI image generation guide](https://developers.openai.com/api/docs/guides/image-generation)

## Skill Output:

**Output Type(s):** [Image files, Text, Guidance, Shell commands]

**Output Format:** [JSON shape specifications, transparent PNG markup and previews, optional black-and-white masks, and prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markup images match the source dimensions; the skill also guides submission and review of the resulting image edit.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
