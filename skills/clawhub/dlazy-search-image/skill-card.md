## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users use this skill to search for image URLs and metadata for reference images, backgrounds, and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches, prompts, parameters, and referenced media files may be sent to dLazy-hosted services.

Mitigation: Avoid submitting private, confidential, or sensitive material unless the user's data handling requirements allow use of the dLazy service.

Risk: The CLI stores API credentials locally and can use them for hosted requests.

Mitigation: Use a revocable API key, rotate or revoke it when no longer needed, and prefer per-invocation credentials or npx when a persistent setup is not desired.

Risk: The --save option can write downloaded assets to the local filesystem.

Mitigation: Use explicit safe output paths and review destinations before running commands that save files.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are returned by the dLazy CLI as JSON containing image URLs and metadata; asynchronous mode can return a task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
