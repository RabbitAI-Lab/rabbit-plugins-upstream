## Description:

Adapts web novels into webtoon drama plans and per-episode scripts, with optional dLazy CLI image-generation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn web-novel material into Chinese-language webtoon adaptation outputs, including genre confirmation, plot breakdowns, episode tags, and episode scripts. Users may also invoke dLazy CLI workflows for related image generation when they intentionally want that integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media paths may be sent to dLazy services for external processing.

Mitigation: Use the skill only with manuscripts and media suitable for that external processing, and avoid unpublished or sensitive material unless approved.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Prefer short-lived or scoped credentials where available, use the DLAZY_API_KEY environment variable for temporary use, and rotate or revoke keys when no longer needed.

Risk: Installing or running the npm CLI executes third-party package code with the user's normal account permissions.

Mitigation: Install only when dLazy CLI integration is intended, keep the package version pinned, and review the package/source before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-webtoon-adapter)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown and structured Chinese prose with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are returned in conversation; optional dLazy CLI calls can return externally hosted media URLs.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
