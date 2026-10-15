## Description:

Helps agents generate PixVerse C1 videos from text, reference images, or first and last frames using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, reference images, or first and last frames through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy's hosted service, and generated assets are hosted remotely.

Mitigation: Only submit content you are authorized to share; review the service terms before using sensitive material.

Risk: Logging in can persist an API key in the local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY when local key persistence is undesirable, and rotate or revoke stored keys when needed.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated video results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional saving of the returned asset.]

## Skill Version(s):

1.2.30 (source: ClawHub release; artifact frontmatter lists 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
