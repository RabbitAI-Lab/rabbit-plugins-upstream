## Description:

Selects a dLazy video model for text, image, or media-driven video generation and provides commands to run it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select and run dLazy video-generation models for text-to-video, image-to-video, frame-guided video, digital humans, and lip-sync tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy, and generated files are hosted by dLazy.

Mitigation: Review prompts and media for sensitive content before submission and check dLazy's handling of hosted outputs.

Risk: Logging in can store an API key locally, and the skill uses an external npm CLI.

Mitigation: Use the pinned CLI version, choose npx to avoid a global install, and rotate or revoke the API key when needed.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is returned through dLazy-hosted URLs.]

## Skill Version(s):

1.4.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
