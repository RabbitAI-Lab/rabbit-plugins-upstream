## Description:

fal.ai sync-lipsync v3 generates a new video whose speaker lip movement is synchronized to a supplied audio track for dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content-production agents use this skill to invoke dLazy's hosted lip-sync generation CLI with video and audio inputs, then receive generated media URLs or async task IDs for dubbing and localization workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI that may be globally installed.

Mitigation: Prefer the pinned npx command or an unprivileged sandbox, and review the package before installation.

Risk: The dLazy API key is a credential stored locally or passed through the environment.

Mitigation: Limit local config access, avoid exposing the key in logs or prompts, and rotate or revoke it if compromise is suspected.

Risk: Video and audio inputs are uploaded to dLazy-hosted services for processing.

Mitigation: Only pass media files that are approved for upload to dLazy and appropriate for the user's account and workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return dLazy file URLs or async task IDs; local video or audio paths supplied to the CLI are uploaded for cloud processing.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
