## Description:

PixVerse C1 video model for text-to-video, image-to-video, first/last-frame-to-video, and reference-to-video generation, with strengths in action, VFX, and high-motion scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted PixVerse C1 video-generation service from an agent workflow. It supports prompt-driven video generation plus image, first-frame/last-frame, and reference-image workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media paths supplied to image, video, or audio fields are sent to dLazy's hosted service.

Mitigation: Pass only media files intended for upload and use the service only when hosted processing is acceptable.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied by environment variable.

Mitigation: Keep the key revocable, rotate it when needed, and remove it from the local configuration when access is no longer required.

Risk: A global CLI install persists a third-party binary on the user's system.

Mitigation: Use the pinned npx invocation or a sandbox when avoiding a persistent global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON, files]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted file URLs; with --save, the CLI can download the result asset to a local path.]

## Skill Version(s):

1.2.15 (source: server release evidence; artifact frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
