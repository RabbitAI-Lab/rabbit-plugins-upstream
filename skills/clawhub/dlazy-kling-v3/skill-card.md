## Description:

Generates videos with Kling v3 from text prompts or reference images using the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Kling v3 video-generation CLI for text-to-video and image-to-video jobs, including optional asynchronous polling and saving generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI that stores a dLazy API key locally and sends requests to dLazy services.

Mitigation: Install only if you trust dLazy and its npm package, avoid running the CLI as administrator, and rotate the dLazy API key if CLI compromise is suspected.

Risk: Local media paths passed to image, video, or audio fields may be uploaded to dLazy media storage for generation.

Mitigation: Review which local files are passed to the CLI and avoid sending sensitive media unless the dLazy account and service terms are acceptable for the use case.

Risk: A global npm install persists a CLI binary on the system.

Mitigation: Prefer npx or a sandboxed environment when a persistent global install is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated media URLs, asynchronous task IDs, and optionally save generated assets to a local path.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
