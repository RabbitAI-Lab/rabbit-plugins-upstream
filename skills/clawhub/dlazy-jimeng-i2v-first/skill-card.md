## Description:

Generate dynamic videos from a single first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to call dLazy's Jimeng image-to-video service with a prompt and first-frame image, then receive generated media URLs or save the resulting asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a pinned third-party npm CLI and sends prompts, parameters, and selected media files to dLazy cloud endpoints.

Mitigation: Review the linked CLI source or npm package before use, prefer the npx invocation when possible, and only submit media that is appropriate for dLazy's service.

Risk: Generation requests require a dLazy API key and may consume credits.

Mitigation: Use a revocable API key, store it through the CLI or per-invocation environment variable, rotate it when needed, and run with --dry-run to confirm estimated cost before billable requests.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted media URLs, asynchronous task identifiers, or a locally saved generated asset when --save is used.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
