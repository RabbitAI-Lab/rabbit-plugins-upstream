## Description:

分镜脚本 Storyboard helps agents use dLazy's storyboard template to create multi-shot animated videos from scripts, character references, shot prompts, voice, music, effects, and subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to start or continue dLazy storyboard projects for consistent-character, multi-shot animated shorts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Do not submit confidential or regulated content unless the user's organization has approved dLazy for that data.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: Use OS account protections, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation environment variables for short-lived use.

Risk: Installing a global CLI creates persistent local supply-chain exposure.

Mitigation: Review the CLI source when supply-chain risk matters and use the pinned npx invocation when a persistent global binary is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and terminal-oriented text with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated storyboard project state, uploaded file URLs, and hosted video-generation results returned by dLazy.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
