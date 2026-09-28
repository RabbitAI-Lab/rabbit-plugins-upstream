## Description:

Helps users generate short videos from prompts and optional image, video, or audio references through the dLazy Seedance 2.5 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, optionally using media references or first and last frames to guide the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation runs a third-party npm package.

Mitigation: Confirm you trust dLazy and the npm package publisher before installing.

Risk: The CLI may store a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Prompts and provided media are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media unless the service's handling is acceptable for the task.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns generated-media URLs; optional saving downloads the result locally.]

## Skill Version(s):

1.2.18 (source: ClawHub release metadata; artifact install instructions pin dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
