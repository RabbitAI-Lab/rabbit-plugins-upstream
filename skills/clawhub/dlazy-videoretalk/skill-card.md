## Description:

Video Retalk uses the dLazy CLI and hosted API to create a lip-synced talking-person video from a source video and new speech audio, with optional reference-face selection for multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy VideoRetalk jobs that align a person's mouth movements in a video to replacement speech audio. It is useful for dubbed or revoiced talking-head video and can target a specific face when a reference image is supplied.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the dLazy npm CLI and hosted API for execution.

Mitigation: Review the pinned CLI package and service terms before use; use npx for one-off runs when a global install is not desired.

Risk: The skill requires an API key that may be stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Protect the key from prompts, logs, and shared shells, and rotate or revoke it from the dLazy dashboard if exposure is suspected.

Risk: Selected videos, audio, face images, prompts, and parameters are sent to dLazy's hosted service.

Mitigation: Use only media and prompts approved for the intended organization and service before running generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous task identifier; local media paths supplied to the CLI are uploaded to dLazy's hosted service.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
