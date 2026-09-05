## Description:

Generate coherent transition videos using Jimeng's first and tail frame models from supplied first-frame and last-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Jimeng first-tail image-to-video workflow, providing a prompt plus first and last frame images to generate a transition video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy account and can spend dLazy credits when generation requests are submitted.

Mitigation: Use --dry-run for cost estimates when appropriate and confirm the account has enough credits before running generation.

Risk: Local media passed as frame inputs is uploaded to dLazy-hosted services for model processing.

Mitigation: Avoid private or sensitive media unless the user accepts the cloud upload and third-party processing.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx when persistence is not desired, and rotate or revoke keys from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [CLI guidance and JSON responses containing generated asset URLs; optional local file output when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may return asynchronous task status when --no-wait is used.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
