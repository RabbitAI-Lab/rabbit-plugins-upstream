## Description:

fal.ai sync-lipsync v3 generates a new video where a speaker's lip movement matches a provided audio track, supporting dubbing, localization, and virtual presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content production teams use this skill to invoke a hosted lip-sync generation workflow that aligns an input video's mouth movement to an input audio track. It is suited to dubbing, localization, and re-syncing virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external npm CLI and requires a dLazy API key.

Mitigation: Review the pinned CLI package before installation and store or rotate the API key using the documented dLazy account controls.

Risk: Local video or audio files passed to the CLI may be uploaded to dLazy services for processing.

Mitigation: Use only media that is approved for hosted processing and avoid submitting sensitive content unless the relevant data handling terms allow it.

Risk: The reviewed artifact contains documentation mistakes around output type and example flags.

Mitigation: Confirm required command flags with `dlazy sync-lipsync-3 -h` before execution and validate returned output before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted output URLs or an asynchronous task identifier.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
