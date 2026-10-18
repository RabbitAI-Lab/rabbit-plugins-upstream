## Description:

Turns a script or shot list into a storyboarded, shot-by-shot video using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video teams use this skill to turn scripts into multi-shot animated videos with storyboards, character references, audio, subtitles, and a final render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to dLazy's hosted service.

Mitigation: Share only content approved for the service and review attachments before sending.

Risk: Authentication uses a dLazy API key stored in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: The workflow installs or invokes a pinned external CLI.

Mitigation: Review the CLI before use and choose the on-demand npx option if a global install is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text responses and Markdown guidance with shell commands; the hosted service can produce storyboard and video assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based conversations support follow-up edits and attached reference files.]

## Skill Version(s):

1.0.27 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
