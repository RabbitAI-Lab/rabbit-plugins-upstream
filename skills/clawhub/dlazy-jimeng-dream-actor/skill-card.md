## Description:

Convert static character images into action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Jimeng Dream Actor service from an agent or shell workflow, supplying a prompt plus one image or video reference to generate an action-video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths supplied to the skill may be uploaded to dLazy's hosted API and media storage.

Mitigation: Use the skill only with data appropriate for dLazy's cloud service and avoid submitting sensitive media unless the user has approved that transfer.

Risk: API use may consume dLazy credits.

Mitigation: Use dry-run mode to review payloads and cost estimates before submitting generation requests.

Risk: Persisting a global CLI or saved API key increases local credential exposure.

Mitigation: Prefer the pinned npx command for one-off use and supply DLAZY_API_KEY per invocation when persistent local config is not desired.

## Reference(s):

- [dLazy CLI source code](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses containing hosted output URLs; optional downloaded media files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimation, asynchronous task IDs, polling, timeout control, and optional result saving.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
