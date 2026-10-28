## Description:

HeyGen Lipsync Speed: Fast lip-sync model, ideal for scenarios requiring rapid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize an input video's lip movements with supplied audio, with optional captions and audio or duration adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local media is uploaded to dLazy for processing, and generation may incur charges.

Mitigation: Review the media before submitting and proceed only if comfortable sending it to dLazy; use --dry-run to inspect the cost estimate.

Risk: The dLazy API key is stored locally when using the CLI login flow.

Mitigation: Use device-code login or environment-based credentials, keep API keys out of chat, and revoke stored keys when no longer needed.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)

## Skill Output:

**Output Type(s):** [Media files, JSON]

**Output Format:** [JSON result containing generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can run asynchronously when --no-wait is used.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
