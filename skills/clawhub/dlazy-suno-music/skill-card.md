## Description:

Generates Suno music from prompts in inspiration or custom modes, including vocal or instrumental tracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate music through the dLazy CLI, choosing automatic lyrics, manual lyrics, vocals, instrumentals, and output download behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI may persist an API key in a local configuration file without enforcing the file permissions described by the skill artifact.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive keys, or manually restrict permissions on ~/.dlazy/config.json after using login or auth set.

Risk: The installed dlazy binary is a broader cloud-tool CLI, not only the Suno music command.

Mitigation: Review the dLazy CLI before global installation and consider npx @dlazy/cli@1.2.3 for on-demand use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [CLI commands and JSON result envelopes with generated media URLs; optional downloaded output files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; supports dry-run, asynchronous generation, timeout, and local save options.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
