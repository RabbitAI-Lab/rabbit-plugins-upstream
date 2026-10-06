## Description:

Helps agents generate Jimeng images from text prompts through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate images from text prompts, optionally with reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media may be sent to dLazy, with generated images hosted by dLazy.

Mitigation: Avoid sending sensitive prompts or files without authorization and review the service terms before use.

Risk: API calls may consume account credits.

Mitigation: Check the estimated cost with the dry-run option before submitting a request.

Risk: The CLI may persist an API key in local configuration.

Mitigation: Use a revocable key or supply DLAZY_API_KEY per invocation to reduce persistent credential storage.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown or text with shell commands and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted image URLs or an asynchronous task ID; images can optionally be saved locally.]

## Skill Version(s):

1.3.25 (source: server-resolved release; bundled skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
