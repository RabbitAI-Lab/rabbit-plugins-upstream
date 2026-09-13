## Description:

Generate dynamic videos based on a single first frame image and prompts using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to call the dLazy Jimeng image-to-video service from an agent workflow, supplying a first-frame image, prompt, duration, and output handling options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy hosted API and file endpoints for generation.

Mitigation: Use the skill only with prompts and media that are appropriate to share with the dLazy service.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the API key like any credential and rotate or revoke it from the dLazy dashboard if exposure is suspected.

Risk: Running the skill depends on the third-party dLazy npm CLI.

Mitigation: Prefer npx or a reviewed pinned install and avoid administrator privileges when invoking the CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI can return hosted result URLs, save generated assets to a requested path, or return an async generation ID for later polling.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
