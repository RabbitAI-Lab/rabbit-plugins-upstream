## Description:

Happy Horse 1.0 video model covers text-to-video, first-frame-to-video, reference-to-video, and video editing by routing the selected mode to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Happy Horse 1.0 hosted video-generation service from an agent workflow. It supports prompt-based generation, first-frame or reference-image generation, and video editing through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the pinned dLazy npm CLI and a hosted dLazy API.

Mitigation: Install only the pinned CLI version documented by the release, review the package or source before use, and run it in environments appropriate for third-party SaaS calls.

Risk: Prompts, parameters, and local media paths supplied to image, video, or audio options may be uploaded to dLazy services.

Mitigation: Avoid sending sensitive private media or prompts unless that is acceptable under the user's dLazy account policy and service terms.

Risk: The skill requires a dLazy API key that may be stored locally or passed through DLAZY_API_KEY.

Mitigation: Use appropriate organization keys, restrict local config access, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON responses from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or save generated assets to a local path when requested.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
