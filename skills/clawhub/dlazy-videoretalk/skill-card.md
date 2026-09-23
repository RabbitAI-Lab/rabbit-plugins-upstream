## Description:

Tongyi VideoRetalk lip-syncs a talking-person video to a supplied voice audio track, with an optional reference face image for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content-production agents use this skill to submit a talking-person video, voice audio, and optional face reference to dLazy's hosted VideoRetalk service for lip-sync video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video, audio, and optional face-reference media are uploaded to dLazy's hosted service for processing.

Mitigation: Use the skill only with media you are authorized to process and avoid sensitive content unless the service terms and data-handling posture meet your requirements.

Risk: The dLazy API key may be stored in the local CLI configuration or supplied through the environment.

Mitigation: Use a revocable key, rotate it when needed, and prefer per-run DLAZY_API_KEY for tighter control in shared or ephemeral environments.

Risk: A global CLI install leaves a persistent executable on the machine.

Mitigation: Use the pinned npx invocation when a persistent global CLI is not desired.

Risk: The security summary notes documentation inconsistencies.

Mitigation: Check `dlazy videoretalk -h` and use `--dry-run` where appropriate before making service calls.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON service responses containing generated media URLs or async task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated media to a local path when the CLI is invoked with --save.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
