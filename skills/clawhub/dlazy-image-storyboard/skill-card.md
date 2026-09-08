## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, educators, and agents use this skill to turn creative briefs into structured storyboard plans, character references, panel prompts, and delivery specifications before rendering images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on installing or invoking the external dLazy npm CLI.

Mitigation: Review the package source and prefer sandboxed or local npx execution before allowing persistent global installation.

Risk: Prompts and referenced media may be sent to dLazy API and file-hosting services.

Mitigation: Avoid sensitive prompts, confidential media, unrelated local files, and secrets when using the skill.

Risk: Creative prompts may be interpolated into terminal commands.

Mitigation: Invoke the CLI with safe argument handling and avoid shell-string construction for untrusted prompt text.

Risk: The workflow requires a dLazy API key stored in local configuration or passed through the environment.

Mitigation: Use a limited, revocable API key and rotate or revoke it from the dLazy dashboard when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with storyboard plans, structured panel prompts, CLI command examples, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation at key gates before image generation; uses dLazy API and hosted file URLs for generated media.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
