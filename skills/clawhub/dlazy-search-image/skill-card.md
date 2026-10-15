## Description:

Helps agents find image assets and report image URLs and metadata through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to look up reference images, backgrounds, and other design assets by keyword and receive image links and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-search description does not fully convey the hosted dLazy API and generation-style behavior.

Mitigation: Review the service behavior and returned results before relying on it as a direct image search.

Risk: Using the service requires a dLazy API key and may send prompts, parameters, and referenced local media files to dLazy-hosted services.

Mitigation: Use only approved credentials and content; avoid private file paths unless you intend to upload those files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI (declared homepage)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Image URLs and metadata in an agent response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying service may return JSON results or an asynchronous task ID.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
