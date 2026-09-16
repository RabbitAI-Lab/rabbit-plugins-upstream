## Description:

Video Replicate extracts the first frame and audio from a source video, uses video understanding to produce a prompt, and returns a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to have an agent run dLazy's video-replicate CLI on source videos and retrieve a Seedance 2.0 replication bundle with media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external npm CLI can introduce dependency or publisher trust risk.

Mitigation: Verify that you trust dLazy and the pinned @dlazy/cli package before use; prefer npx for one-off execution when a persistent global install is unnecessary.

Risk: Local media supplied to the skill is uploaded to dLazy cloud endpoints for processing.

Mitigation: Only provide videos, images, or audio that are appropriate to upload to dLazy's hosted service.

Risk: The dLazy API key is a credential stored locally or supplied through DLAZY_API_KEY.

Mitigation: Use OS user-restricted config storage or per-invocation environment variables, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or a downloaded asset file when --save is used; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
