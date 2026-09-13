## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, supporting text-to-video, first/last-frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos with the dLazy MiniMax H3 service from text prompts, frame transitions, or image, video, and audio references. It is suited for agent workflows that need cloud-hosted video generation through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media are sent to dLazy hosted endpoints for generation.

Mitigation: Pass only media files intended for upload to dLazy and review the service terms before use.

Risk: Installing or running the dLazy CLI introduces ordinary npm supply-chain and SaaS dependency risk.

Mitigation: Install only if the dLazy CLI package and service are trusted; prefer the pinned npx invocation when a global executable is not needed.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use a revocable dLazy API key, rely on OS user file permissions, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON CLI response with generated media URLs; optional downloaded media file when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with --no-wait and local file upload for media reference inputs.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter declares 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
