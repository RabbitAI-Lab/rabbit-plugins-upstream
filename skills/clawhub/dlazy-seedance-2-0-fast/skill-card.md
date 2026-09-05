## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos faster with support for multi-modal references, first/last frame, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent generate short videos through dLazy's hosted Seedance 2.0 Fast API, using text prompts and optional image, video, audio, first-frame, or last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media passed to the skill may be uploaded to dLazy's hosted API and media storage.

Mitigation: Avoid sending sensitive private media unless that data sharing fits the use case and the user has reviewed dLazy's service terms.

Risk: Authentication can persist a dLazy API key in local CLI configuration.

Mitigation: Use the npx invocation or DLAZY_API_KEY for less persistent setup, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses may include generated media URLs, asynchronous task identifiers, or saved local output paths.]

## Skill Version(s):

1.3.11 (source: release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
