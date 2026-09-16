## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan, generate, and iterate logo concepts, derivatives, and brand identity system assets through a staged dLazy CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow asks the agent to install or run an external npm CLI.

Mitigation: Prefer the npx invocation where possible, verify the package and source before use, and avoid unnecessary global installation.

Risk: The workflow requires a dLazy API key that may be stored in local CLI configuration or passed through the environment.

Mitigation: Use a revocable API key, keep it out of shared logs and files, and rotate or revoke it when access is no longer needed.

Risk: Logo prompts and selected media files may be sent to dLazy API and file-hosting endpoints.

Mitigation: Avoid uploading sensitive client assets or confidential brand material unless the user has approved that data flow.

Risk: Install and data-flow documentation is reported as inconsistent in the security evidence.

Mitigation: Confirm the intended CLI version and data handling path before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-logo-branding-system)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with staged prompts, todo/status summaries, shell commands, and generated asset URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke the dLazy CLI/API and return hosted result URLs; selected media inputs may be uploaded through the CLI.]

## Skill Version(s):

1.2.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
