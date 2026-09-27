## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan social-media carousel image sets, confirm direction once, approve the cover first, and then generate matching remaining slides through the dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a dLazy API key and may store credentials in the local CLI configuration.

Mitigation: Use environment-based credentials when saved configuration is not desired, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Prompts and referenced media files may be sent to dLazy-hosted services for generation.

Mitigation: Avoid submitting sensitive prompts or media unless the user is comfortable with dLazy processing and hosting generated outputs.

Risk: The skill depends on the @dlazy/cli package and may incur API usage costs.

Mitigation: Review the package and pinned version before installation, and confirm expected API usage costs before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, status updates, prompts, CLI commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user confirmation gates before image generation and sends prompts or referenced media to dLazy-hosted services when the CLI is run.]

## Skill Version(s):

1.3.21 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
