## Description:

Happy Horse 1.0 generates and edits video through dLazy's hosted API, supporting text-to-video, first-frame-to-video, reference-to-video, and video editing modes with automatic routing to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to invoke dLazy's Happy Horse 1.0 service for video generation and editing from prompts, reference images, first frames, or source videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected media files are sent to dLazy cloud endpoints for generation.

Mitigation: Confirm the user intends to send those inputs to dLazy before submitting sensitive prompts or media.

Risk: API keys may persist in the local dLazy configuration, and the security evidence notes the storage claim is stronger than what the pinned CLI appears to enforce.

Mitigation: Prefer per-run DLAZY_API_KEY or verify config file permissions after login/auth set; rotate or revoke keys that may have been exposed.

Risk: A global install leaves a pinned third-party CLI on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for one-off invocations when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source repository](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown usage guidance with bash examples and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or download assets when --save is used; asynchronous runs return a generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
