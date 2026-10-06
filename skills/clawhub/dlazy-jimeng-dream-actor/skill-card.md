## Description:

Turns a static character image into an action video using Jimeng Dream Actor through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to animate a character image into an action video using a prompt and optional reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable uploading to dLazy.

Risk: Using the service requires a dLazy API key and may save it locally.

Mitigation: Use the environment-variable flow if you do not want a saved key, and prefer the on-demand CLI if you do not want a global install.

## Reference(s):

- [dLazy CLI source and usage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns media URLs or an asynchronous task ID; the agent can provide a local download path when requested.]

## Skill Version(s):

1.3.25 (source: server-resolved release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
