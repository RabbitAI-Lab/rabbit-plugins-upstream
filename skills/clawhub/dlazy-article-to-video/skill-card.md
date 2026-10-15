## Description:

Turns written articles and documents into narrated explainer videos through the dLazy video-generation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to turn articles or documents into narrated explainer, training, or report videos with a hosted video-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive documents unless dLazy's handling of them is acceptable.

Risk: The skill requires an external npm CLI and may save an API key locally.

Mitigation: Review the CLI before installing, use the pinned npx option to avoid a persistent global installation, and protect the locally saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with CLI commands and project updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is handled by the external dLazy service.]

## Skill Version(s):

1.0.32 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
