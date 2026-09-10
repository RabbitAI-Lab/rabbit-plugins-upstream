## Description:

fal.ai sync-lipsync v3 generates a new video where a speaker's lip movement matches a supplied audio track for dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted lip-sync workflow from an agent, supplying video and audio inputs to generate re-synced video for dubbing, localization, or virtual presenter updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party CLI installation and API-key handling can affect sensitive environments.

Mitigation: Review the linked dLazy CLI source or npm package before installation, prefer npx for one-off use when a global executable is not needed, and rotate or revoke dLazy API keys from the publisher dashboard when required.

Risk: Video, audio, and request parameters are uploaded to dLazy-hosted services for processing.

Mitigation: Avoid sending media that is confidential or restricted unless the user's organization has approved the service terms and data handling posture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [CLI JSON response with hosted media URLs and optional local file download via --save]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; video and audio inputs may be uploaded to dLazy-hosted services for processing.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
