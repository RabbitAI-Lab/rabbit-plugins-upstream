## Description:

Generate coherent transition videos with Jimeng first-and-tail-frame models from a prompt plus supplied first and last frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Jimeng first/tail-frame video CLI, passing a prompt plus first and last frame images to produce a coherent transition video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media may be uploaded to the dLazy cloud service for processing.

Mitigation: Avoid sensitive media unless the user accepts the dLazy service terms and cloud-processing behavior.

Risk: The dLazy CLI may store an API key in a local configuration file.

Mitigation: Use per-invocation credentials when appropriate, protect the local config file, and rotate or revoke API keys from the dLazy dashboard if exposure is suspected.

Risk: Global installation of the third-party CLI persists an executable on the system.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

Risk: The release evidence notes documentation invocation/output mistakes.

Mitigation: Check the current CLI help with dlazy jimeng-i2v-first-tail -h before relying on example commands or output fields.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with hosted media URLs and optional downloaded result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generateId when --no-wait is used; --save can download the generated asset to a local path.]

## Skill Version(s):

1.3.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
