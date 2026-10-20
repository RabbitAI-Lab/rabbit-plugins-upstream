## Description:

Plans social-media carousel slides and guides cover-first image generation with user approval before continuing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media creators and marketing teams use this skill to plan platform-specific carousel slides, approve a cover design, and generate matching subsequent images with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's cloud service.

Mitigation: Review content and obtain permission before uploading sensitive or third-party media.

Risk: The workflow requires a third-party CLI and a locally stored API key.

Mitigation: Review the package before running it, use npx to avoid a persistent global install if preferred, and protect or rotate the API key.

Risk: The supplied skill text lists an older version and inconsistent CLI version information.

Mitigation: Confirm the release and CLI versions before installing or following commands.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image URLs, Shell commands, Guidance]

**Output Format:** [Markdown slide plan and prompts, followed by generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cover-first delivery with user confirmation before generating the remaining slides.]

## Skill Version(s):

1.3.33 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
