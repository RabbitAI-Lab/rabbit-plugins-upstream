## Description:

Video Retalk helps an agent call dLazy's hosted Tongyi VideoRetalk workflow to lip-sync a talking-person video to a supplied voice track, with optional reference-face targeting for multi-person videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate lip-synced person videos from a source talking-head video and a replacement voice track through dLazy's hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected local video, audio, and optional face-reference media to dLazy cloud endpoints for processing.

Mitigation: Use only media that may be shared with dLazy, and review organizational privacy requirements before invocation.

Risk: The dLazy CLI stores or accepts an API key for authenticated requests.

Mitigation: Use the documented login or environment-variable flow, protect the local config file, and rotate or revoke the key from dLazy when needed.

Risk: A global CLI install persists third-party executable code on the system.

Mitigation: Use the pinned npx invocation when avoiding a global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes containing generated media URLs or task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers; saved media files are produced only when the caller uses the CLI save option.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
