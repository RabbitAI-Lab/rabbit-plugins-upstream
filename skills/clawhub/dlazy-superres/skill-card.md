## Description:

Image super-resolution tool that enhances image clarity and detail and returns an upscaled image URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted super-resolution service through the dLazy CLI, sending an image URL or local image and receiving an enhanced image URL or saved file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external dLazy CLI package and hosted dLazy service.

Mitigation: Confirm the package and service are trusted before installing or invoking the CLI.

Risk: Images supplied as local paths can be uploaded to dLazy media storage for processing.

Mitigation: Use only images that are appropriate to send to dLazy's hosted service.

Risk: The dLazy API key may be saved in the user's local CLI configuration.

Mitigation: Treat the saved key as a credential and rotate or revoke it from the dLazy dashboard when needed.

Risk: The artifact contains a documentation inconsistency between the shown `--image` option and an example using `--prompt`.

Mitigation: Check `dlazy superres -h` before use and prefer the documented image input option for image upscaling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs, asynchronous task identifiers, or saved local files through the dLazy CLI.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
