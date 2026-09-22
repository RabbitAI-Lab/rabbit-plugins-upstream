## Description:

全能生成 Generate routes image, video, and audio generation requests to the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to select and run dLazy CLI models for image, video, and audio generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced image, video, or audio files are sent to dLazy cloud services for generation.

Mitigation: Avoid passing sensitive prompts or local files unless the user is comfortable using dLazy's cloud service.

Risk: The dLazy CLI can save an API key in the local user config file.

Mitigation: Use DLAZY_API_KEY for per-session authentication when persistent local credential storage is not desired.

Risk: The skill invokes a third-party CLI and hosted API endpoints.

Mitigation: Install only when third-party API use is acceptable and keep the CLI version pinned as declared by the skill metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or relay generated media URLs hosted by files.dlazy.com; requires a dLazy API key and npm or npx.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
