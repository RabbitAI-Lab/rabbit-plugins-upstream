## Description:

fal.ai sync-lipsync v3 generates a new video where a speaker's lip movement matches a supplied audio track, supporting dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content creators use this skill to run dLazy's hosted lip-sync workflow from an agent, supplying video and audio inputs and receiving a synchronized generated video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input video and audio are uploaded to dLazy's hosted API and media storage.

Mitigation: Use only media appropriate for dLazy's hosted service, and avoid sensitive media unless the user accepts upload and hosted result URLs.

Risk: Authentication relies on a dLazy API key stored locally or supplied through an environment variable.

Mitigation: Use `dlazy login`, `dlazy auth set`, or per-invocation `DLAZY_API_KEY`; rotate or revoke organization keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output containing hosted result URLs or async task identifiers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download the generated video to a local path when --save is used; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
