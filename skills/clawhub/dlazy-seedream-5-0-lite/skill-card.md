## Description:

Generates images with Doubao Seedream 5.0 Lite from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to ask an agent to generate or transform images with Doubao Seedream 5.0 Lite through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and selected local image paths may be sent to a hosted third-party service.

Mitigation: Treat prompts and selected image paths as data shared with dLazy, and avoid submitting sensitive content unless approved for that service.

Risk: The skill depends on the third-party @dlazy/cli npm package and a dLazy API key.

Mitigation: Install only if you trust dLazy and the pinned CLI package, prefer npx or scoped installation when practical, and rotate or revoke the API key if misuse is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON result metadata with hosted image URLs and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous task IDs when invoked without waiting.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
