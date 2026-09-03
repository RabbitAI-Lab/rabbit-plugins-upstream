## Description:

Text-to-image generation with Jimeng that converts prompts and optional reference images into hosted image outputs through the dLazy CLI and API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate images from text prompts, optionally using reference images, through dLazy's Jimeng text-to-image service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local files may be sent to dLazy's hosted API and media storage.

Mitigation: Avoid private prompts and sensitive local files unless the user has approved use of the dLazy hosted service.

Risk: Image generation may incur account charges through dLazy.

Mitigation: Use explicit Jimeng/dLazy wording before invocation, consider --dry-run for cost estimates, and report insufficient-balance errors clearly.

Risk: A saved dLazy API key can be misused if exposed.

Mitigation: Store credentials only through the documented dLazy auth flow or environment variable, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [JSON result containing image output URLs, with optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; --dry-run can estimate cost without calling the API, and --no-wait can return an asynchronous task ID.]

## Skill Version(s):

1.3.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
