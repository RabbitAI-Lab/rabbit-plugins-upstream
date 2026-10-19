## Description:

Guides agents to synchronize video lip movements with audio using dLazy's hosted HeyGen Lipsync Speed service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request fast lip-sync generation from a video and audio source, with options for captions, timing, and audio enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the dLazy CLI runs third-party code.

Mitigation: Review the pinned CLI source before installation or use the on-demand npx option.

Risk: Media supplied for lip-sync is uploaded to dLazy's hosted service.

Mitigation: Only submit media you are comfortable uploading to dLazy.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Rotate or revoke the key when you stop using the service.

## Reference(s):

- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Service responses include hosted output URLs or an asynchronous task ID; an optional flag downloads the resulting asset.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
