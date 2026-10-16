## Description:

Guides agents to generate videos from text prompts and optional image, video, audio, or first-and-last-frame references using dLazy's Seedance 2.0 CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate videos from text or multimedia references and retrieve the resulting assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service, and generated files may be hosted there.

Mitigation: Only submit media and prompts you are comfortable sharing with dLazy; review the selected local paths before generation.

Risk: The CLI needs a dLazy API key to submit generation requests.

Mitigation: Store a key only if you trust the CLI and account controls; use the documented on-demand npx invocation if you prefer not to install it globally.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can be asynchronous; results may be saved locally or retrieved through hosted links.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
