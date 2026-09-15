## Description:

HeyGen Lipsync Speed runs a dLazy-hosted lip-sync generation model optimized for fast video and audio synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content automation agents use this skill to invoke dLazy's HeyGen Lipsync Speed model for fast lip-sync generation from video and audio inputs, with options for captions, dynamic duration, audio enhancement, async polling, and saving generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy-hosted services for processing.

Mitigation: Use only media approved for external processing and review dLazy service terms before sending sensitive or regulated content.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Prefer per-invocation credentials through DLAZY_API_KEY when persistent storage is undesirable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Using this skill depends on trusting the dLazy publisher and the pinned @dlazy/cli package.

Mitigation: Use the pinned npx invocation for non-persistent execution and review the linked source or package before installing a global binary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON results containing generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with polling and can save generated assets to a local path.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
