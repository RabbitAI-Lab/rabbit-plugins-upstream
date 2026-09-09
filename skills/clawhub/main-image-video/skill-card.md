## Description:

Generates a 3-5 second ecommerce main-image video from a single product image, with guidance for camera motion, material motion, backend configuration, and short test runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, content teams, and agent developers use this skill to turn an existing product hero image into a short listing-ready video. The skill is suited to single-image clip generation with explicit backend selection, dry-run review, and manual platform compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider networking can send API credentials and user media to an arbitrary configured Ark endpoint.

Mitigation: Use only trusted provider environment variables, avoid setting ARK_BASE_URL unless the destination is controlled and trusted, and prefer scoped, revocable API keys.

Risk: Product images and prompts are sent to the configured generation provider.

Mitigation: Run dry-run first, confirm the selected provider and model before generation, and avoid submitting sensitive product media unless the provider and account controls are acceptable.

Risk: Generated motion can amplify defects in the source image or distort the product.

Mitigation: Review and repair the static image before generation, start with one short 3-second test clip, use subtle motion prompts, and manually check platform video requirements before publishing.

## Reference(s):

- [Main Image Video skill page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and JSON examples; generation runs save MP4 video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run request preview, explicit video model selection, provider routing, and optional ffmpeg-based concatenation or subtitle handling.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
