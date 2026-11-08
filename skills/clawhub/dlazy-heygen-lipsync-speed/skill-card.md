## Description:

HeyGen Lipsync Speed provides fast lip-sync generation for workflows that need rapid results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the dLazy CLI to generate fast lip-synchronized media from video and audio inputs, with optional captions and audio adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio inputs, including local files, are sent to dLazy's hosted service and media storage.

Mitigation: Use media you are comfortable uploading to dLazy.

Risk: Login stores an organization API key in the local CLI configuration.

Mitigation: Protect the local configuration file; use the documented DLAZY_API_KEY alternative or rotate and revoke the key from the organization dashboard.

Risk: Generation requests may incur service charges.

Mitigation: Review the --dry-run cost estimate and account balance before generating media.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Generated media result URL with JSON result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a completed result or an asynchronous task identifier.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
