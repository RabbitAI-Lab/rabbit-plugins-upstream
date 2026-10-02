## Description:

Helps agents generate and edit videos from text, images, or video using dLazy's Happy Horse 1.0 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent to create videos from prompts or reference images, or to edit an existing video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be uploaded to the dLazy service, and generated outputs are hosted there.

Mitigation: Only submit content authorized for third-party processing and review the service's data-handling terms before use.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use the per-invocation environment variable option if local key storage is unsuitable, and protect or rotate credentials as needed.

Risk: Using the skill requires installing or running a third-party npm CLI.

Mitigation: Review the CLI package and its permissions before installation or execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and generated-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service hosts generated assets; asynchronous requests can return a task ID before results are ready.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
