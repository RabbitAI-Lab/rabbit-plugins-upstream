## Description:

Selects dLazy models to generate images, videos, or audio from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to choose dLazy generation models and create images, videos, speech, music, or sound effects from prompts and optional media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy's hosted service.

Mitigation: Only submit content you are comfortable sharing with dLazy; review local media inputs before use.

Risk: A saved API key may remain accessible in a shared environment.

Mitigation: Prefer per-invocation credentials in shared environments and remove or rotate any stored key when no longer needed.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-generate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Media links]

**Output Format:** [Text with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated media is returned via hosted URLs.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
