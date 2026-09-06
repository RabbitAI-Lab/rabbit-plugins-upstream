## Description:

This skill helps agents run dLazy's hosted fal.ai sync-lipsync v3 workflow to generate a lip-synced video from a source video and audio track for dubbing, localization, or virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create lip-synced video outputs from a selected video and audio track for dubbing, localization, and virtual presenter re-syncing. It is suited to agent workflows that can call the dLazy CLI, provide a dLazy API key, and handle cloud-hosted generated media URLs or saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio media are sent to dLazy's hosted service, and generated outputs are returned from dLazy-hosted media storage.

Mitigation: Use only media that is approved for upload to the service, and review dLazy service terms before using the skill in sensitive workflows.

Risk: A dLazy API key is required and may be stored in the local CLI configuration when using login or auth setup commands.

Mitigation: Prefer DLAZY_API_KEY for one-off use on shared or temporary machines, and rotate or revoke organization API keys when access changes.

Risk: The artifact examples include documentation quality issues that can lead agents to use --prompt instead of the required video and audio inputs.

Mitigation: Invoke the tool with --video_url and --audio_url, and use dlazy sync-lipsync-3 -h to confirm current CLI options before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON result metadata with generated media URLs or saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous runs that return a generateId for polling; --save can download the generated asset to a local path.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
