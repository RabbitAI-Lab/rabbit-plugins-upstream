## Description:

Search for image assets by keyword through dLazy's hosted service and return image URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can find reference images, backgrounds, and design assets by keyword and review image links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches use dLazy's hosted service and require a stored dLazy API key, rather than accessing Pixabay directly.

Mitigation: Use the service only if its data handling is acceptable; rotate or revoke the API key when no longer needed.

Risk: Providing a local media file path can upload that file to dLazy's service.

Mitigation: Avoid local file paths unless you explicitly intend to upload the files.

Risk: Installing the CLI globally or saving a result may affect the local environment.

Mitigation: Prefer the pinned on-demand CLI invocation or review the package before global installation, and choose a safe download destination.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may include image links and metadata; an optional save path downloads an asset.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
