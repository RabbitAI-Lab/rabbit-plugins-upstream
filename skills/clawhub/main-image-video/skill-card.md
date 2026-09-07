## Description:

Turns a single product hero image into a 3-5 second short product video with controlled camera motion and subtle material movement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce operators and creative agents use this skill to convert an existing product main image into a short listing-ready video, usually before batch production or platform review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts can upload local files or fetched image URLs to external generation providers.

Mitigation: Use trusted local asset directories and known image URLs, pin the intended provider, and run --dry-run before paid or networked generation.

Risk: Credentials and product assets may be exposed if the skill is run in sensitive environments or against an uncontrolled endpoint.

Mitigation: Use limited-scope, rotatable API keys and avoid ARK_BASE_URL unless the endpoint is fully controlled.

Risk: Product videos may inherit or amplify flaws from the input image or deviate from platform listing requirements.

Mitigation: Review the static image first, generate one short test clip before batching, and manually check video duration, aspect ratio, size, and marketplace rules.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video Backend Configuration](references/video-backends.md)
- [Provider CLI Reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts and commands for video generation; generated media is saved as MP4 files by the helper scripts.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
