## Description:

HeyGen Lipsync Speed is a dLazy CLI wrapper for fast lip-sync generation from supplied video and audio inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's HeyGen Lipsync Speed service for rapid lip-sync generation. It supports video and audio inputs plus optional captions, dynamic duration, music removal, speech enhancement, partial synchronization, and asynchronous task polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud CLI that stores or reads a dLazy API key.

Mitigation: Authenticate only with a trusted dLazy account, keep the key scoped to the intended organization, and rotate or revoke it from the dLazy dashboard when access is no longer needed.

Risk: Local video or audio inputs may be uploaded to dLazy-hosted endpoints for processing.

Mitigation: Use only media that is appropriate to send to dLazy, and avoid uploading confidential or regulated content unless the user's organization has approved that workflow.

Risk: Global installation persists the dLazy CLI on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for on-demand execution when a persistent global install is not desired.

Risk: Generation can fail because of missing API keys, insufficient credits, unavailable local files, service errors, or asynchronous task failure.

Mitigation: Check authentication and credits before execution, validate local file paths, use dry-run or asynchronous status polling when appropriate, and surface service-returned errors to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [JSON responses with generated output URLs or asynchronous task status, plus concise user-facing guidance for authentication, credits, and errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media inputs may be uploaded to dLazy endpoints; completed results are returned as files.dlazy.com URLs.]

## Skill Version(s):

1.3.9 (source: ClawHub server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
