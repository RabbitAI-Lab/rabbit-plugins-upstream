## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke Jimeng text-to-image generation through the dLazy CLI, sending prompts and optional reference images to the hosted dLazy service and receiving generated image URLs or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided local media files may be sent to the dLazy hosted service.

Mitigation: Use only content suitable for dLazy processing, and avoid sensitive prompts or media unless the user's policy permits sending them to the service.

Risk: Generated results are hosted on files.dlazy.com.

Mitigation: Treat returned URLs as externally hosted outputs, and avoid generating or uploading sensitive content unless external hosting is acceptable.

Risk: Login can store a dLazy API key locally, and API calls may consume credits.

Mitigation: Prefer secure local config handling or per-invocation DLAZY_API_KEY where appropriate, and use --dry-run to inspect payload and cost before generation when useful.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration guidance]

**Output Format:** [JSON response with generated image URLs or async task status; optional saved image file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and explicitly provided media may be sent to dLazy, and generated assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
