## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, educators, and agent operators use this skill to turn creative briefs into structured cinematic or narrative storyboards with gated planning, character approval, script approval, and staged image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Prefer DLAZY_API_KEY for per-session credentials or manually restrict permissions on ~/.dlazy/config.json.

Risk: Prompts and attached media may be uploaded to dLazy cloud endpoints.

Mitigation: Avoid attaching private media unless the user intends to upload it to dLazy.

Risk: Image generation commands can run from the agent environment.

Mitigation: Confirm each render command before execution and review the @dlazy/cli package or source before use in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, storyboard specifications, prompt drafts, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires staged user confirmations before character generation, script progression, and each image-generation command.]

## Skill Version(s):

1.3.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
