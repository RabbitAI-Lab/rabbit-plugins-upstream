## Description:

Happy Horse 1.0 is a dLazy video-generation skill for text-to-video, first-frame-to-video, reference-to-video, and video editing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to call the dLazy Happy Horse 1.0 hosted video-generation model from an agent. It supports prompt-only generation, first-frame generation, reference-image generation, and video editing through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media files are sent to the dLazy API and media storage.

Mitigation: Only submit prompts and media that are acceptable to upload to dLazy, and review dLazy terms before use.

Risk: The dLazy CLI can save an API key in the user's local configuration.

Mitigation: Use DLAZY_API_KEY for one-off use when local persistence is not desired, and rotate or revoke organization keys when needed.

Risk: Installing the external @dlazy/cli package adds third-party executable code.

Mitigation: Review the pinned @dlazy/cli package or source before global installation, or use npx for on-demand execution.

Risk: The artifact sample output shows an image result even though the skill is for video generation.

Mitigation: Validate returned output type and MIME type in downstream workflows before treating the result as video.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with CLI commands; CLI responses are JSON containing generated media URLs or async task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted on files.dlazy.com. Async mode can return a generateId for polling.]

## Skill Version(s):

1.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
