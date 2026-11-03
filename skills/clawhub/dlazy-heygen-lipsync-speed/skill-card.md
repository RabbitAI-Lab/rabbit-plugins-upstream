## Description:

Creates fast lip-synced video using the HeyGen Lipsync Speed model through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers can submit video and audio to generate a lip-synced video, with options for captions, timing, and audio enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and audio supplied as local paths are uploaded to dLazy media storage for processing.

Mitigation: Submit only media you are authorized to share with dLazy, and review the service terms before uploading.

Risk: Generation may incur charges.

Mitigation: Use the documented --dry-run option to preview the request and estimated cost before generation.

Risk: Authentication stores an API key in the local CLI configuration, and the published executable and service-side data handling are outside this artifact review.

Mitigation: Review the pinned CLI before installation, protect the local configuration, and rotate or revoke exposed keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy](https://dlazy.com)
- [dLazy API key page](https://dlazy.com/dashboard/organization/api-key)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated lip-synced video asset with JSON result metadata, returned as a hosted URL or saved file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation and optional captions, duration adjustment, background music removal, and speech enhancement.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
