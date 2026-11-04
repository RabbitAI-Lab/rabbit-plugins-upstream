## Description:

Happy Horse 1.0 video model — one model covers text-to-video (t2v), first-frame-to-video (i2v), reference-to-video (r2v), and video editing (edit), routing each mode to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate or edit short videos from text prompts, a first frame, reference images, or an existing video, and receive the resulting media or its hosted URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and its external CLI and service were not fully verified in the security review.

Mitigation: Use the service only if you trust dLazy with the prompts and media you submit, and review the CLI package or project information before installing it.

Risk: The CLI stores an API key in its local configuration, and video generation may incur usage costs.

Mitigation: Protect the local configuration, rotate or revoke the key if needed, and use --dry-run to inspect the cost estimate before submitting a generation request.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Media assets, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON results with hosted media URLs, plus shell-command and configuration guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media may be downloaded to a local path; asynchronous requests can return a task ID for later status checks.]

## Skill Version(s):

1.3.37 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
