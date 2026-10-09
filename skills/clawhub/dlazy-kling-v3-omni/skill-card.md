## Description:

Helps agents generate videos from prompts and optional reference media using Kling v3 Omni through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from text prompts and optional image, video, or audio inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy-hosted services.

Mitigation: Confirm the content is appropriate to share with dLazy before generating or uploading.

Risk: Using the external CLI can install software globally and store a dLazy API key locally.

Mitigation: Review the CLI before use, prefer on-demand npx when a global install is unnecessary, and rotate or revoke the key when no longer needed.

## Reference(s):

- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text guidance and JSON results containing generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task status and optional local download.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
