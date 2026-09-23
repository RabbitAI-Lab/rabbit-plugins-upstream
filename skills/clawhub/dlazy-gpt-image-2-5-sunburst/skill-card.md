## Description:

GPT Image 2.5 Sunburst, the precision tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing for detailed creative work with reference images, multiple aspect ratios, and quality settings up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy hosted GPT Image 2.5 Sunburst service for image generation or editing from prompts, optional reference images, aspect ratio settings, and quality settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy's hosted service, and generated assets are hosted by dLazy.

Mitigation: Use the skill only for content suitable for dLazy's hosted service and avoid sending sensitive media or prompts unless the service terms and data handling are acceptable.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication or rotate and revoke organization keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy binary on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses containing generated image URLs or asynchronous task status, with optional downloaded image files when a save path is provided.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted files.dlazy.com URLs; asynchronous runs may return a generateId for later polling.]

## Skill Version(s):

1.2.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
