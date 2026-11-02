## Description:

A text-to-vector model that creates artwork for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to generate scalable vector-style artwork, including logos and icons, from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and submitted media are sent to dLazy's hosted service for processing.

Mitigation: Submit only content appropriate for that service and review its terms before use.

Risk: Generation may consume paid credits.

Mitigation: Use --dry-run to preview the request and estimated cost before generation.

Risk: The CLI stores an API key in local configuration or accepts one through an environment variable.

Mitigation: Keep the key private and revoke it when it is no longer needed.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Vector artwork]

**Output Format:** [Generated image asset URL; the documented response example is PNG]

**Output Parameters:** [One prompt with an optional aspect ratio]

**Other Properties Related to Output:** [The asset can be downloaded to a local path.]

## Skill Version(s):

1.3.34 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
