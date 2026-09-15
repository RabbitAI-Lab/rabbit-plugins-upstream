## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Vidu Audio Clone service with a reference audio file and prompt, producing generated speech audio through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can be misused for impersonation or consent violations.

Mitigation: Use only voices you own or have clear permission to clone, and do not use generated audio for impersonation or identity-check bypass.

Risk: The skill depends on a third-party CLI package and hosted dLazy services.

Mitigation: Review the package or source before installation, keep the CLI pinned as declared, and avoid installing or running npm commands with elevated privileges.

Risk: Reference audio and prompts are sent to dLazy endpoints and local media files may be uploaded.

Mitigation: Send only audio and prompts appropriate for the dLazy service and your privacy requirements, and avoid uploading sensitive or unauthorized voice data.

Risk: dLazy API credentials are required for use.

Mitigation: Store keys through the documented CLI configuration or environment variable flow, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
