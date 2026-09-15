## Description:

Convert static images into dynamic videos using Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to call dLazy's Vidu Q2 image-to-video service, supplying prompts and image inputs to generate dynamic video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI and hosted service receive the user's prompt, API key, and media files explicitly passed to the command.

Mitigation: Install only when that trust boundary is acceptable, prefer the pinned npx invocation or user-level install, and rotate the dLazy API key if exposure is suspected.

Risk: Running npm installation or CLI commands with elevated privileges can expand the impact of a compromised package or credential.

Mitigation: Avoid elevated privileges for npm and dLazy CLI commands, and keep authentication in the normal user-level dLazy configuration or per-invocation environment variable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated media URLs or asynchronous task identifiers; the CLI can also save generated assets to a local path.]

## Skill Version(s):

1.3.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
