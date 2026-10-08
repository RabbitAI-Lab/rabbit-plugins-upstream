## Description:

Guides agents in generating Seedance 2.0 videos from text prompts, media references, or first and last frames through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos using text prompts, image, video, or audio references, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and generated media is hosted there.

Mitigation: Review inputs before submission and avoid sending sensitive prompts or media without approval.

Risk: The third-party CLI can be installed globally and authentication can store an API key locally.

Mitigation: Review the CLI before installing, use the on-demand npx option to avoid a persistent global install, and rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI commands; the CLI returns JSON containing generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can run asynchronously; completed media is hosted by dLazy and can be saved locally.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; bundled frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
