## Description:

Generate dynamic videos from a single first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate a short Jimeng image-to-video result from a prompt and a first-frame image through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to third-party dLazy endpoints for generation.

Mitigation: Use only media and prompts approved for upload to dLazy, and confirm the account/API-key requirements before use.

Risk: The CLI can save an API key in local user configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx when less local persistence is desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact examples use an --image flag while the documented command help uses --firstFrame.

Mitigation: Run dlazy jimeng-i2v-first -h and use the current documented flag before invoking generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI repository declared in metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated media URLs are returned by the hosted service, and local media inputs may be uploaded to dLazy endpoints.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
