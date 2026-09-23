## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Q2 image-to-video service from an agent workflow, passing prompts and image inputs to generate dynamic video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive media or confidential prompts unless the user accepts dLazy's service terms and cloud processing model.

Risk: Login or auth setup can save a dLazy API key in a local CLI config file.

Mitigation: Use per-invocation environment variables when persistence is not desired, restrict access to the local config, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated outputs are hosted on files.dlazy.com.

Mitigation: Review generated output URLs and retention expectations before using the skill with private or regulated content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, asynchronous task IDs, or downloaded output files when the --save option is used.]

## Skill Version(s):

1.3.19 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
