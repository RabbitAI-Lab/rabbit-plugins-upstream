## Description:

Guides an agent to upscale images with the dLazy CLI and return a link to the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to improve low-resolution images and retrieve an enhanced image URL or saved file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images passed to the CLI may be uploaded to the dLazy hosted service.

Mitigation: Submit only images approved for external processing and confirm the input before running the command.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Prefer device-code login or careful secret handling; avoid sharing the key and revoke it if exposed.

Risk: The documented image flag and example prompt flag conflict, which could lead to a failed or unintended request.

Mitigation: Check `dlazy superres -h` and use `--dry-run` to confirm parameters before submitting an image.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and image result URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe an optional local download or asynchronous task ID.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
