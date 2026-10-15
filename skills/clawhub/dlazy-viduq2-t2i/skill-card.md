## Description:

Generate images from text prompts or reference images using Vidu Q2 through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts, optionally supplying reference images and choosing aspect ratio and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images supplied to the skill may be uploaded to dLazy's cloud service.

Mitigation: Share only inputs you are comfortable sending to dLazy; review its service terms before use.

Risk: Logging in may save an API key on the local device.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication if you do not want a saved key.

Risk: A global CLI installation persists software on the local device.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 option if you do not want a persistent global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Files]

**Output Format:** [JSON response with hosted image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous mode returns a task ID for later polling instead of immediate image URLs.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
