## Description:

Routes image, video, and audio generation requests to an appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can route image, video, or audio creation requests through dLazy's CLI and receive generated media. The skill also supports passing outputs between generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted service.

Mitigation: Submit only prompts and files you are authorized to share with that service.

Risk: CLI authentication can save an API key in the local user configuration.

Mitigation: Protect the configuration and operating system account; rotate or revoke the key if it is exposed. Review the pinned CLI before installing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, URLs, JSON]

**Output Format:** [Generated media hosted at URLs, with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quality, dimensions, duration, and other settings vary by selected model.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
