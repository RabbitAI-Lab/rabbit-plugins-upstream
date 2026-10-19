## Description:

Helps agents request fast text-to-video and reference-guided video generation through dLazy's Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts, reference media, or first and last frames through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service.

Mitigation: Use only prompts and media approved for upload to a third-party service.

Risk: The CLI may save an API key in local configuration.

Mitigation: Use a per-invocation API key environment variable when persistent credential storage is unsuitable.

Risk: Running the third-party CLI introduces an external software dependency.

Mitigation: Review the pinned @dlazy/cli package and linked source before installation if your environment requires third-party CLI approval.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hosted media links or asynchronous task IDs.]

## Skill Version(s):

1.3.30 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
