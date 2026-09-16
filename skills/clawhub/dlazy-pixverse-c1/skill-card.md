## Description:

PixVerse C1 is a dLazy video-generation skill for text-to-video, image-to-video, first/last-frame-to-video, and reference-image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy PixVerse C1 hosted API from an agent workflow and generate short videos from prompts, image references, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI may store an API key in local user configuration.

Mitigation: Use environment variables for per-invocation credentials where appropriate, rotate or revoke keys from the dLazy dashboard, and protect local config files.

Risk: Prompts and media file paths passed to the skill are sent to dLazy services, and local media inputs may be uploaded.

Mitigation: Avoid submitting sensitive prompts or media unless the user accepts the dLazy hosted API data flow.

Risk: Global npm installation leaves a persistent executable on the system.

Mitigation: Prefer npx or an isolated environment when persistent global installation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, downloaded asset paths, or asynchronous task identifiers through the dLazy CLI.]

## Skill Version(s):

1.2.17 (source: server release metadata; artifact frontmatter says 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
