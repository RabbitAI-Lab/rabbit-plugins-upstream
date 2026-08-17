## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos from static images, reference images, or first and last frames through the dLazy Vidu Q2 CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted API and media storage.

Mitigation: Use only media appropriate for dLazy's service, confirm the selected dLazy/Vidu Q2 skill before upload, and avoid private images unless approved.

Risk: Authentication may rely on a globally installed CLI and saved API key.

Mitigation: Prefer npx or per-run DLAZY_API_KEY when avoiding persistent installs or stored credentials, and rotate or revoke keys from dLazy if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated result is returned as hosted media URLs, or as an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
