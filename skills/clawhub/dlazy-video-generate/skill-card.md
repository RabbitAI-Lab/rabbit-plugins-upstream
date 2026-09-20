## Description:

Generates AI videos by selecting an appropriate dLazy CLI video model for text-to-video, image-to-video, frame-to-video, digital human, and lip-sync workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create short videos from prompts, images, frame pairs, reference media, or audio-driven lip-sync requests through the dLazy cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy cloud endpoints for generation.

Mitigation: Use only content approved for third-party cloud processing and review dLazy service terms before sensitive use.

Risk: Authentication can save a dLazy API key in local CLI configuration.

Mitigation: Protect the local config file, prefer per-invocation environment variables when appropriate, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: A global CLI install persists a third-party package on the user's system.

Mitigation: Use the pinned npx invocation when avoiding a global install, and review the third-party CLI/package before use in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON envelopes from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by dLazy; local media inputs may be uploaded through the CLI.]

## Skill Version(s):

1.4.19 (source: server release metadata; artifact frontmatter lists 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
