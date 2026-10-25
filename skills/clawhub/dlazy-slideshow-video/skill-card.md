## Description:

Turn slides or a document into a narrated slideshow video with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators can use the skill to turn presentation slides or documents into narrated explainer, report, courseware, or training videos. It guides a dLazy hosted agent through new or existing video projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents are sent to dLazy's hosted service, and attached files are uploaded to its media storage.

Mitigation: Only submit documents and messages you are comfortable sharing with dLazy; avoid sensitive material.

Risk: Login stores an organization API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it may have been exposed.

Risk: Continuing an existing project can use its saved context, and video generation may consume credits.

Mitigation: Check the selected project before continuing and confirm available credits before generation.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [CLI project link listed by the skill (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Video]

**Output Format:** [Chat guidance and commands, with narrated slideshow video deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and attached files are sent to dLazy's hosted service; review project selection before continuing, and be aware that video generation may consume credits. The bundled review does not audit the external CLI or hosted service.]

## Skill Version(s):

1.0.30 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
