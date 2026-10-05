## Description:

Guides agents to generate videos with Seedance 2.5 using text prompts, media references, and first/last-frame control through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request generated video clips from text prompts or image, video, audio, and frame references via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI requires trusting its execution on the user's device.

Mitigation: Review the CLI and use the version-pinned install or on-demand invocation described in the skill.

Risk: A dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Protect the key and rotate or revoke it from the dLazy account dashboard if needed.

Risk: Prompts and user-selected media files are sent to dLazy's hosted service.

Mitigation: Only submit prompts and media approved for external processing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown command guidance and JSON results with generated media URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally save generated media locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.2.21 (source: ClawHub release metadata; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
