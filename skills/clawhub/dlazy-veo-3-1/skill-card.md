## Description:

Generates cinematic video outputs with Google Veo 3.1 from text prompts, image inputs, or video extension requests through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create or extend videos with Google Veo 3.1 via the dLazy hosted service. It supports prompt-based generation, first/last-frame generation, reference-image generation, asynchronous task polling, and saving generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths supplied to the CLI can be uploaded to the dLazy cloud service for generation.

Mitigation: Use the skill only with media and prompts that are appropriate for a third-party hosted service, and avoid sending private or regulated content unless the service terms and account controls are acceptable.

Risk: The CLI may store an API key in a local configuration file.

Mitigation: Prefer per-invocation credentials or the pinned npx command when persistent installation is not desired, and rotate or revoke the API key from the dLazy dashboard if access changes.

Risk: Generated assets are hosted by dLazy and may consume paid credits.

Mitigation: Review the linked CLI package and service account settings before using paid credits or generating sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs; async requests can return a task identifier for later polling.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
