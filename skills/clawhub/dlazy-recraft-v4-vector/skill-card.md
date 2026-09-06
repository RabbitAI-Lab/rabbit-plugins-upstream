## Description:

Generates SVG vector artwork from text prompts for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and agents use this skill to call dLazy's Recraft V4 Vector model for logo, icon, and scalable vector asset generation from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media paths supplied to the CLI are processed through dLazy's cloud service.

Mitigation: Use only prompts and files approved for dLazy cloud processing, and review applicable service terms before sending sensitive or regulated content.

Risk: A saved dLazy API key can consume organization credits and may persist in local configuration.

Mitigation: Prefer per-run `DLAZY_API_KEY` or `npx` when avoiding persistent local state; when using `dlazy login` or `dlazy auth set`, check `~/.dlazy/config.json` permissions and rotate exposed keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses; generated assets are returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous generation and optional local save paths.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
