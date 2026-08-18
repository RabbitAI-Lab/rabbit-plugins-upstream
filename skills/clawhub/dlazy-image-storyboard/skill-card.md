## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, educators, and agents use this skill to plan cinematic or narrative storyboard projects, prepare panel prompts, run approved dLazy image-generation commands one at a time, and assemble final storyboard deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI may store an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-run credentials when local persistence is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Installing a global npm CLI can increase local supply-chain exposure.

Mitigation: Review the dLazy CLI source or npm package before installation, or use the pinned npx invocation instead of a global install.

Risk: Local media paths supplied to the CLI may be uploaded to dLazy-hosted services for model processing.

Mitigation: Only provide media files that are appropriate to upload to dLazy, and avoid sensitive or restricted content unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before each generation command; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
