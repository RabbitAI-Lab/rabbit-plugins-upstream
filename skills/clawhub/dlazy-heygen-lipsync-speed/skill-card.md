## Description:

Guides agents in generating fast lip-synced video using the dLazy-hosted HeyGen Lipsync Speed service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize a video's lip movements with supplied audio through dLazy's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the external CLI and storing or passing a dLazy API key exposes credentials if the installation or local environment is not trusted.

Mitigation: Review the pinned CLI package before installation and protect the API key; rotate or revoke it if compromised.

Risk: Local video and audio supplied to the command are uploaded to dLazy's cloud service.

Mitigation: Only submit media approved for external processing and review the service terms before use.

Risk: The example uses --prompt although the documented options emphasize video and audio inputs.

Mitigation: Check the installed CLI's help for the correct flags before running a generation request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Command guidance and JSON responses containing generated-media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID or save the resulting media locally.]

## Skill Version(s):

1.3.24 (source: server release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
