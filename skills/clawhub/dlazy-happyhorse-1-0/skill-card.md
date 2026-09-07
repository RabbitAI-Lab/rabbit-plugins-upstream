## Description:

Happy Horse 1.0 generates and edits video through dLazy, supporting text-to-video, first-frame-to-video, reference-to-video, and video-editing modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Happy Horse 1.0 model from an agent workflow to create or edit videos from prompts, images, or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires trusting the pinned @dlazy/cli npm package.

Mitigation: Review the package before use and prefer the on-demand npx invocation when a persistent global binary is not desired.

Risk: Prompts and selected local media are sent to dLazy services for generation.

Mitigation: Avoid sending sensitive media or prompts unless dLazy's service terms and data handling are acceptable for the use case.

Risk: Authentication depends on a dLazy API key that may be stored in local CLI configuration or supplied by environment variable.

Mitigation: Protect the local config file, use per-invocation environment variables when appropriate, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Files, Guidance]

**Output Format:** [JSON response with generated media URLs, task status for async runs, and optional saved video files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload prompt-selected local media to dLazy and return files.dlazy.com URLs; --no-wait returns an async generateId.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
