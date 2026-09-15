## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request short video generation or video extension from Google Veo 3.1 Fast via dLazy. It supports prompt-based generation, first/last-frame guided generation, optional video extension, asynchronous task polling, and saving returned media locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, generation parameters, and selected local media files to dLazy's hosted service.

Mitigation: Only pass prompts and media paths intended for upload to dLazy, and avoid using sensitive or regulated content unless the deployment has approved that data flow.

Risk: All requests require a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use device-code login where possible, avoid pasting API keys into shell history, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The install path uses a pinned third-party npm CLI package that can be installed globally.

Mitigation: Confirm trust in dLazy and the pinned @dlazy/cli package before installing; prefer npx or another isolated execution path when persistent global installation is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing generated media URLs or asynchronous task identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-supplied local media paths to dLazy storage and may save generated media to a local path when requested.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
