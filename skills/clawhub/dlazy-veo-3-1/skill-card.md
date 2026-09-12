## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or extend cinematic videos through the dLazy CLI using prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and referenced media may be sent to the dLazy hosted API and media storage.

Mitigation: Use the skill only with data approved for third-party cloud processing, and avoid submitting sensitive prompts or media unless that use is authorized.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Store credentials under the intended OS user account, prefer per-invocation environment variables where appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Global installation of the third-party dLazy CLI persists executable code on the system.

Mitigation: Review the referenced source or package before installation and prefer npx or an unprivileged environment when persistent installation is not required.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, downloaded files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.15 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
