## Description:

音乐生成 Suno Music helps agents generate Suno music through the dLazy CLI, supporting inspiration mode, custom lyrics mode, vocals, and instrumental output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run the dLazy Suno music generation CLI from an agent, passing prompts and music parameters to create songs or instrumental tracks through the hosted dLazy API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI can persist an API key in the local user config, and the security evidence notes that claimed file-permission protection was not confirmed in the inspected CLI package.

Mitigation: Prefer per-invocation DLAZY_API_KEY when key persistence is not desired, or verify that ~/.dlazy/config.json is readable only by the current OS user after login or auth setup.

Risk: Prompts, generation parameters, and user-supplied media paths may be sent to dLazy services, and generated assets are hosted remotely.

Mitigation: Avoid sending sensitive prompts or media unless the user accepts dLazy service handling, and review returned asset URLs before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses from the dLazy CLI, including generated asset URLs and optional saved media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts and referenced media are sent to dLazy services.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
