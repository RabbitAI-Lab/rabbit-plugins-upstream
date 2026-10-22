## Description:

Generates images, videos, and audio by selecting an appropriate dLazy CLI model based on the user's intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create images, videos, and audio from natural-language requests through dLazy models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy-hosted services, and generation consumes service credits.

Mitigation: Submit only content approved for external processing, review expected costs, and monitor usage.

Risk: The external CLI package was not fully audited.

Mitigation: Review the pinned package before installation or execution, and use device login or environment-variable authentication where practical. Revoke stored API keys when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, Video, Audio]

**Output Format:** [Generated media assets, returned as URLs in JSON CLI envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multiple outputs and command piping are supported; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
