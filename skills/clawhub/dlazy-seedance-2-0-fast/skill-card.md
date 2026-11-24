## Description:

Generates videos with Seedance 2.0 Fast from prompts and optional multimodal references or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from text prompts, image, video, or audio references, or first and last frames through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because some referenced material was unavailable, so the review may not cover all related content.

Mitigation: Treat the review as incomplete and inspect the referenced CLI materials before installing or using the skill.

Risk: Prompts and supplied media are sent to dLazy's hosted API, and local media files may be uploaded for processing.

Mitigation: Send only prompts and media you are permitted to share with the service, and remove sensitive content first.

Risk: Using the skill requires a dLazy API key stored through the CLI authentication flow or supplied per invocation.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON result metadata]

**Output Format:** [Hosted video asset URLs with JSON result or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation supports 4–12 second durations; results may be returned asynchronously.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
