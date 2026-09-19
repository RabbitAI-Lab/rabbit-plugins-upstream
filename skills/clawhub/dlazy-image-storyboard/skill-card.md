## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creatives, producers, educators, and developers use this skill to turn creative briefs into gated storyboard plans, character references, panel prompts, generated image URLs, and final storyboard assembly guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends storyboard prompts and any supplied media to dLazy cloud services.

Mitigation: Avoid submitting confidential media unless the user accepts dLazy's cloud processing terms and the project permits external processing.

Risk: The workflow requires a dLazy API key that may be stored in local CLI configuration or passed through an environment variable.

Mitigation: Use the documented login or key setup flow, keep the key out of shared logs and files, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The artifact text contains stale package-version wording alongside the current install command.

Mitigation: Confirm the intended @dlazy/cli version before installation; use the npx option when a persistent global CLI install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bullet lists, inline shell commands, structured storyboard prompts, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses confirmation gates before generation and may produce dLazy-hosted media URLs.]

## Skill Version(s):

1.3.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
