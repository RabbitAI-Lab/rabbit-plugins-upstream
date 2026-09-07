## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1 from text prompts, reference images, frame pairs, or video extension inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for Veo 3.1 video generation, including text-to-video, image-guided generation, frame-pair generation, and video extension workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party hosted service and sends prompts, parameters, and referenced media to dLazy endpoints.

Mitigation: Use it only for content appropriate for the dLazy service, avoid sensitive prompts or private media, and review dLazy's terms before production use.

Risk: The skill uses an npm CLI that may be installed globally and stores or reads a dLazy API key from local configuration or the DLAZY_API_KEY environment variable.

Mitigation: Prefer the pinned npx invocation when possible, review the linked source before global installation, protect local configuration files, and rotate or revoke the API key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return hosted result URLs, asynchronous generation IDs, or save generated media to a local path when requested.]

## Skill Version(s):

1.3.13 (source: evidence.release; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
