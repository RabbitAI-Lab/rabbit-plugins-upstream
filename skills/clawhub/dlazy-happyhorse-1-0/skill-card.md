## Description:

Happy Horse 1.0 video model covers text-to-video, first-frame-to-video, reference-to-video, and video editing modes through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit video through the dLazy Happy Horse 1.0 model from prompts, reference images, first frames, or source videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party CLI that calls an external cloud API.

Mitigation: Review the linked source or npm package before use, and prefer npx when avoiding a persistent global installation.

Risk: Prompts and supplied media files are sent to dLazy API and media storage endpoints.

Mitigation: Only provide media intended for upload to dLazy and avoid submitting sensitive content unless approved for that service.

Risk: The skill requires a dLazy API key for authenticated requests.

Mitigation: Use a revocable dLazy API key, store it through the CLI or environment variable, and rotate or revoke it from the dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON metadata for generated assets and may return asynchronous task identifiers.]

## Skill Version(s):

1.3.15 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
