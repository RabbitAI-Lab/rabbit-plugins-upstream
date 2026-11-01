## Description:

Happy Horse 1.0 video model — one model covers text-to-video (t2v), first-frame-to-video (i2v), reference-to-video (r2v), and video editing (edit).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the dLazy CLI to generate videos from text, animate a first frame, create videos from reference images, or edit existing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media are sent to dLazy and media may be stored on its hosting service.

Mitigation: Upload only media you intend to send to dLazy.

Risk: Video generation may incur usage charges.

Mitigation: Use --dry-run to preview the request and estimated cost.

Risk: The login flow stores an API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment variable when you prefer not to store the key there.

Risk: Installing the skill's third-party CLI executes external software.

Mitigation: Review the CLI source before installing it.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON API response]

**Output Format:** [Generated video asset URLs and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return asynchronously; results can include a task ID and hosted media URLs.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
