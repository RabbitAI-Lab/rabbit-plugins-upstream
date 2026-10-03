## Description:

Helps agents enhance low-resolution images through dLazy super-resolution and return a URL for the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and other users can enhance low-resolution image assets and retrieve a hosted result URL or save the enhanced image locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images supplied for enhancement are uploaded to dLazy-hosted services.

Mitigation: Obtain approval before submitting sensitive images and review the service's data handling terms.

Risk: The dLazy CLI can save an API key in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if persistent storage is undesirable; rotate or revoke keys when needed.

Risk: Using the skill requires installing or running an external npm package.

Mitigation: Review the pinned package and linked CLI source before installation; use the pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns an enhanced-image URL; optional --save downloads the result locally.]

## Skill Version(s):

1.3.25 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
