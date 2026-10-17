## Description:

Searches for images by keyword through dLazy and returns image URLs and metadata for creative reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, creators, and developers use this skill to find image URLs and metadata for reference images, backgrounds, and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Although advertised as Pixabay image search, the skill uses a dLazy account and intermediary service.

Mitigation: Review dLazy's service and data handling before enabling searches.

Risk: Search terms and explicitly provided local media paths can be sent to dLazy; use requires an API key.

Mitigation: Avoid sensitive queries and local file paths unless intended for upload; protect and rotate the API key.

Risk: Installing the CLI globally persists software on the local system.

Mitigation: Consider the pinned npx invocation instead of a global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON with image URLs and metadata; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous searches may return a task ID before results are ready.]

## Skill Version(s):

1.3.31 (source: ClawHub release; skill files list 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
