## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's hosted video replication workflow from an agent, supplying a reference video and optional parameters to generate a Seedance 2.0 replicate bundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced video or audio files are sent to dLazy-hosted services for processing.

Mitigation: Use the skill only with media and prompts that are appropriate to send to dLazy, and avoid broad stdin or pipeline references that may include secrets or unrelated conversation data.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through the environment.

Mitigation: Use scoped organization keys, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables in shared environments.

Risk: A global npm install persists the pinned dLazy CLI on the system.

Mitigation: Prefer the pinned npx invocation or an isolated environment when persistent global tooling is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses containing generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task IDs for polling; saved media files may be downloaded when a save path is supplied.]

## Skill Version(s):

1.3.16 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
