## Description:

Turns slides or a document into a narrated slideshow-style video with voiceover and transitions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn documents, slides, PDFs, or images into narrated slideshow videos through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Attach only files that are appropriate to upload to the service, and review the service terms before use.

Risk: Authentication commands may store a dLazy API key in the local CLI configuration.

Mitigation: Protect the local config file, use the DLAZY_API_KEY environment variable for per-invocation credentials when preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the pinned dLazy CLI on the user's system.

Mitigation: Use the pinned npx invocation when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted service responses and reference uploaded files through dLazy project sessions.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
