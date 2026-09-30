## Description:

Helps agents turn still images into short videos with Vidu Q2 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate short videos from reference images or first and last frames, with optional prompts and audio settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy cloud services, and generated outputs are hosted there.

Mitigation: Confirm the service is trusted and obtain permission before submitting sensitive prompts or media.

Risk: The dLazy CLI requires an API key and can save it in local configuration.

Mitigation: Use DLAZY_API_KEY per invocation if persistent key storage is undesirable; rotate or revoke exposed keys.

Risk: Running the third-party CLI executes code outside the skill text.

Mitigation: Review the pinned dLazy CLI before installation; use its pinned npx invocation to avoid a persistent global install.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI repository (listed in skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain hosted output URLs; asynchronous jobs require status polling.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
