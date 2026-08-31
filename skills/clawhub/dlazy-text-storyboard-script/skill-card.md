## Description:

Generates detailed short-video storyboard scripts from user themes, structured copy, or outlines while preserving the spoken script text word for word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and video production teams use this skill to turn structured copy or outlines into shot-by-shot storyboard scripts with video parameters, scene descriptions, camera movement, notes, shooting technique, and spoken script allocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is advertised as text-only storyboard writing but also includes behavior that can lead an agent to install or use the dLazy CLI.

Mitigation: Review the release before installing and use it only when the external dLazy workflow is intended.

Risk: The external workflow can store a dLazy API key locally and send prompts or referenced media to dLazy services.

Mitigation: Use controlled API credentials, avoid sensitive prompts or media unless approved for dLazy processing, and rotate or revoke keys when needed.

Risk: Generated result URLs are hosted by dLazy services.

Mitigation: Confirm that generated outputs and any referenced media are suitable for external hosting before use.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown storyboard script with video parameters and repeated shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes default 9:16 and 720p video settings when the user does not provide aspect ratio or resolution.]

## Skill Version(s):

1.2.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
