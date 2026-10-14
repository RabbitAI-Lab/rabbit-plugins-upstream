## Description:

Selects dLazy models to generate or edit images, videos, and audio from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose and run dLazy generation tools for images, videos, and audio, including edits and chained media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI requires installation and access to dLazy-hosted services.

Mitigation: Review the CLI package and service terms before installing or using it.

Risk: API keys can persist in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for less persistent credentials and rotate or revoke keys when needed.

Risk: Prompts, parameters, selected local media, and generated results pass through dLazy-hosted services.

Mitigation: Confirm before uploading files and avoid submitting sensitive content without authorization.

Risk: Generation requests may consume paid API credits.

Mitigation: Check expected costs and available credits before running paid requests.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (package metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Media URLs]

**Output Format:** [Text guidance and CLI JSON results linking to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include image, video, or audio URLs; local downloads depend on the selected command.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
