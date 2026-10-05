## Description:

Helps turn a product image into a short ecommerce listing video using a selected video generation provider.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and content creators use this skill to plan and generate short product-image videos for listing placements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be sent to the selected external provider.

Mitigation: Confirm the provider and model, and share only images and prompts approved for that provider.

Risk: Untrusted image URLs can reference private-network resources.

Mitigation: Use trusted image sources; avoid untrusted URLs that could point to private networks.

Risk: Generation can incur charges or produce inaccurate product details.

Mitigation: Preview with dry-run, test one short clip before batching, and review the video and platform requirements before publishing.

Risk: Suggested CLI installation commands may install third-party software.

Mitigation: Review any installation commands and packages before executing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/main-image-video)
- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with prompt examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow can save a generated MP4 or preview a request with dry-run.]

## Skill Version(s):

1.0.13 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
