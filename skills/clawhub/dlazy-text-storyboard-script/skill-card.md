## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving spoken-script text verbatim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and video production teams use this skill to turn structured short-form video copy or outlines into shot-by-shot storyboard scripts with scenes, camera movement, notes, technique, spoken script, and basic video parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes instructions to install and run a third-party dLazy CLI even though the skill is presented as storyboard text generation.

Mitigation: Treat dLazy CLI media generation as opt-in; execute commands only when the user explicitly wants dLazy media generation and has reviewed the command.

Risk: Prompts and selected media files may be sent to dLazy services when the CLI is used.

Mitigation: Avoid sensitive, confidential, or regulated content in prompts and media files unless the user has approved that transfer.

Risk: The CLI requires npm or npx and an API key stored in local configuration or passed through the environment.

Mitigation: Review the @dlazy/cli package and permissions before installation, prefer pinned on-demand execution where appropriate, and rotate or revoke API keys when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown storyboard script with structured sections and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes basic video parameters and shot-by-shot fields; spoken script is expected to preserve user copy verbatim.]

## Skill Version(s):

1.2.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
