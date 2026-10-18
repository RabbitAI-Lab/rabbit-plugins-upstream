## Description:

Helps agents generate Kling V3 videos from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in generating videos from text prompts or images with Kling V3 via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media may be uploaded to dLazy, and generated files are hosted there.

Mitigation: Use only content suitable for the hosted service and review dLazy's terms before uploading sensitive media.

Risk: The CLI may store a revocable API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if compromised.

Risk: Installing the CLI globally persists a third-party executable.

Mitigation: Prefer the pinned npx command or review the pinned CLI package and source before global installation.

## Reference(s):

- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown guidance and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with generated media URLs; results can optionally be saved locally.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
