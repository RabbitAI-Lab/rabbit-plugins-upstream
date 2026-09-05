## Description:

ElevenLabs music_v1 model generates 10-300 second original music from a natural-language prompt for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to ask an agent to generate original music through the dLazy-hosted ElevenLabs music_v1 service. It is suited for creating background music, advertising tracks, and short-video soundtracks from concise natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and intentionally supplied file paths may be sent to dLazy services for generation.

Mitigation: Use the skill only when cloud processing by dLazy is acceptable, and avoid submitting sensitive prompts or files unless that use is approved.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Prefer `DLAZY_API_KEY` for per-run credentials when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists the pinned `@dlazy/cli` package on the system.

Mitigation: Review the pinned package or source before installation, or use `npx @dlazy/cli@1.2.3` for on-demand execution.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text, markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent invokes a pinned dLazy CLI command and may receive hosted output URLs or an asynchronous generation task identifier.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
