## Description:

Generates video from a first-frame image and text prompt using Jimeng through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from a supplied first-frame image and prompt through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied images may be sent to dLazy's hosted service.

Mitigation: Only submit content authorized for upload to dLazy endpoints.

Risk: Login stores an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if exposed.

Risk: The pinned CLI package requires supply-chain trust, and the documented image flag differs between help and examples.

Mitigation: Review the pinned CLI package and source before installing; check CLI help to confirm the input flag before running.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source (linked in skill metadata; not verified as skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns a generated asset URL or an asynchronous task ID; the CLI can save the asset locally.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
