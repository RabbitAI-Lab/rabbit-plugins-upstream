## Description:

Generates AI images from text prompts using GrusAI API models nano-banana-fast and gpt-image-2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leonrard](https://clawhub.ai/user/leonrard)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate images from text prompts and optional reference images through GrusAI API-backed models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference image URLs, data URLs, or local images may be exposed in logs or transcripts.

Mitigation: Use only non-sensitive reference images until logging is changed to avoid printing private URLs or encoded image data.

Risk: API-returned image download URLs are accepted without independent validation.

Mitigation: Run the skill in a network-contained environment and only use API responses from a trusted GrusAI account and endpoint.

Risk: A leaked or overbroad API key could allow unauthorized image-generation usage.

Mitigation: Use a limited GrusAI API key and rotate it if logs, transcripts, or shared environments may have exposed it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leonrard/skills/image-generator)
- [GrusAI nano-banana API endpoint](https://grsaiapi.com/v1/draw/nano-banana)
- [GrusAI gpt-image-2 API endpoint](https://grsaiapi.com/v1/draw/completions)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with bash command examples, generated image files, and API-returned image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save PNG files and print progress, status, and returned image URLs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
