## Description:

Helps agents generate or edit videos with Happy Horse 1.0 using text prompts, a first frame, reference images, or an existing video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video, first-frame-to-video, reference-to-video, and video-editing jobs through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to the dLazy service; local media inputs are uploaded.

Mitigation: Avoid submitting private prompts or media unless you intend to share them with dLazy.

Risk: The dLazy CLI uses an API key, which may be saved to local configuration.

Mitigation: Use DLAZY_API_KEY for per-run credentials when you do not want a saved key.

Risk: The skill invokes an external CLI package.

Mitigation: Review the pinned CLI package and its source before installation in supply-chain-sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source (tooling; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed jobs return hosted media URLs; asynchronous jobs return a task ID, and results can be downloaded locally.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
