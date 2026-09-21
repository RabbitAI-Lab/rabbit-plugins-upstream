## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Vidu Q2 image-to-video CLI from an agent, supplying prompts and reference images or frames to generate hosted media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are uploaded to dLazy services for inference and storage.

Mitigation: Use only images, prompts, and related media that are approved for upload to dLazy services.

Risk: The skill requires a dLazy API key and may store it in the local CLI configuration.

Mitigation: Use the documented login or environment-variable flow, and rotate or revoke the API key when the skill is no longer used.

Risk: The release installs or runs the pinned @dlazy/cli package.

Mitigation: Review the pinned package and declared source before installing or executing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task IDs, or a saved local output when --save is used.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
