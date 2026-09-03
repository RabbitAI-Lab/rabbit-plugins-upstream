## Description:

Converts static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Vidu Q2 image-to-video service from an agent workflow, supplying prompts and reference images or frames and receiving generated media URLs or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid dLazy API key may be stored in the local CLI configuration.

Mitigation: Use `DLAZY_API_KEY` per invocation when persistent credential storage is not desired, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Prompts, parameters, and local media files are sent to dLazy API and file storage for generation.

Mitigation: Only pass media and prompt content that the user is comfortable uploading to dLazy's service.

Risk: The referenced CLI did not confirm the skill's claim that the key file is restricted to only the current OS user.

Mitigation: Review installation on shared or multi-user systems and inspect local config file permissions after authentication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown usage guidance with CLI commands and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted on files.dlazy.com; the CLI can save returned assets locally with --save.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
