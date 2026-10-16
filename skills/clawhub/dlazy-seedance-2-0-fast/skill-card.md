## Description:

Generates videos from text prompts, optional image, video, and audio references, or first and last frames through dLazy's Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short AI-generated videos from text or supplied media references and retrieve the resulting media link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media are sent to dLazy's hosted service.

Mitigation: Review prompts and media for sensitive content before submission.

Risk: The skill uses a third-party npm CLI and a dLazy API key.

Mitigation: Use npx if a persistent global installation is not desired; rotate or revoke the API key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI project (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Video links]

**Output Format:** [JSON result with a generated-media URL or asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media can optionally be downloaded to a local file.]

## Skill Version(s):

1.3.29 (source: ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
