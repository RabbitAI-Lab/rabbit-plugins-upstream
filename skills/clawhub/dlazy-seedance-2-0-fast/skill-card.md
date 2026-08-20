## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos faster with support for multi-modal references, first and last frames, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to invoke the dLazy CLI for Seedance 2.0 Fast video generation from prompts, reference media, or first and last frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-supplied media paths are sent to dLazy services for cloud video generation.

Mitigation: Avoid sending sensitive prompts or media unless the user's data handling requirements permit dLazy cloud processing.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use per-invocation environment variables when persistent storage is undesirable, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the dLazy command on the user's system.

Mitigation: Use the pinned npx invocation when a one-time command is preferred over a global install.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON with generated media URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by files.dlazy.com; no-wait mode returns a task ID for polling.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
