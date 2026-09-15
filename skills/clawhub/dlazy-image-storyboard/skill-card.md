## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams, agencies, educators, and agent operators use this skill to turn narrative briefs into structured cinematic or narrative storyboards. It guides requirements gathering, character reference development, script approval, image generation, and final storyboard assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs a third-party CLI package.

Mitigation: Review the dLazy CLI package before installing and prefer npx or a project-local, sandboxed install when possible.

Risk: Prompts and referenced media may be sent to dLazy services for generation.

Mitigation: Use the skill only with content appropriate for dLazy processing and avoid sending unrelated, confidential, or sensitive files.

Risk: User-controlled prompt text could be interpolated unsafely into shell commands.

Mitigation: Pass prompt text through safe argument handling and run generation commands synchronously without shell chaining.

Risk: The dLazy API key may be stored in local configuration or provided through an environment variable.

Mitigation: Protect local configuration files, avoid exposing unrelated environment variables, and rotate or revoke API keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured bullets and inline bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Storyboard outputs may include approved visual prompts, generation commands, hosted result URLs, and final layout guidance.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
