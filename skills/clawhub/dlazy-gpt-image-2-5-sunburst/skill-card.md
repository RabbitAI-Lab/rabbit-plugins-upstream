## Description:

GPT Image 2.5 Sunburst, the precision tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing through the dLazy hosted CLI/API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with GPT Image 2.5 Sunburst through the dLazy CLI, including reference images, aspect ratio selection, quality settings, async generation, and saving outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and reference media paths provided to the CLI may be sent to the dLazy hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or media unless the dLazy service terms and data handling are acceptable for the workflow.

Risk: Login may save a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable or npx invocation when less local credential persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated outputs are hosted by dLazy and returned as URLs.

Mitigation: Review generated asset URLs and storage expectations before using the skill for confidential or regulated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results are returned as dLazy-hosted image URLs and can be saved to a local path with the CLI.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
