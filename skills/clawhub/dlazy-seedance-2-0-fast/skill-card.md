## Description:

Helps agents generate videos with Seedance 2.0 Fast from text prompts and optional image, video, audio, or frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request generated videos from text prompts, multimedia references, or first and last frames through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to a third-party generation service.

Mitigation: Confirm the service is trusted and avoid submitting sensitive prompts or media.

Risk: Authentication may store an API key locally.

Mitigation: Protect the local key or use per-invocation credentials, and rotate or revoke compromised keys.

Risk: Video generation may consume paid credits.

Mitigation: Check the cost estimate before running billable generations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and generated-media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
