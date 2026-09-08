## Description:

Generates 10-300 second original music from a natural-language prompt using the ElevenLabs music_v1 model for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's ElevenLabs music generation workflow, authenticate with a dLazy API key, and retrieve or save generated music outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running a third-party CLI can execute package-manager code on the user's machine.

Mitigation: Review the linked dLazy CLI source and package before installing, avoid administrator privileges, and prefer on-demand or least-privileged execution where practical.

Risk: Prompts, parameters, and local media paths passed to the CLI may be sent to dLazy API and media storage services.

Mitigation: Only submit prompts and files that are appropriate to upload to dLazy-hosted services.

Risk: The dLazy API key is a service credential that may be stored in local configuration or supplied through an environment variable.

Mitigation: Protect the key like other service credentials and rotate or revoke it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports async task polling and saving generated assets to a local path.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
