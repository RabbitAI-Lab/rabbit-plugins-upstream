## Description:

Guides an agent to generate Kling V3 Omni videos from text prompts and optional image or video references through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text prompts and optional visual references, then retrieve the generated result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be uploaded to dLazy for generation.

Mitigation: Confirm the material is appropriate to share with dLazy before submitting it.

Risk: Authentication may save a dLazy API key locally.

Mitigation: Protect the key and rotate or revoke it through the dLazy dashboard if needed.

Risk: Installing the third-party CLI grants it access to supplied inputs.

Mitigation: Confirm you trust dLazy and its CLI before installing; use the documented npx option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation returns a result URL or an asynchronous task ID; results can optionally be saved locally.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
