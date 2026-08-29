## Description:

Fast image generation with Doubao Seedream 5.0 Lite, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent invoke the dLazy CLI for fast image generation with Doubao Seedream 5.0 Lite, including text-to-image and image-to-image requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted service for generation.

Mitigation: Do not include private prompts or local files unless you intend them to be uploaded and processed by dLazy.

Risk: Authentication uses a dLazy API key that may be saved in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication when you do not want a saved key, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated assets may be downloaded to a local path selected by the user.

Mitigation: Use --save only with an intended destination path.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned as hosted file URLs and can be downloaded locally with --save.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
