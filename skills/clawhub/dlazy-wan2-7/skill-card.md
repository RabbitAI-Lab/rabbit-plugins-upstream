## Description:

Helps agents create Wan 2.7 videos from text prompts, first and last frames, or reference images and videos through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text, frame pairs, or reference media through dLazy's Wan 2.7 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to the third-party dLazy service.

Mitigation: Use only media and prompts approved for third-party upload; invoke the skill only when dLazy processing is intended.

Risk: Logging in may store an API key in local CLI configuration.

Mitigation: Protect local credentials, use a per-invocation API key when appropriate, and rotate or revoke exposed keys.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown and JSON responses with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns media URLs; optional commands can save generated assets locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
