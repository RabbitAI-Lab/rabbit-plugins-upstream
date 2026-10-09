## Description:

Helps create multi-shot animated shorts with consistent characters, from scripts and shot prompts through generated images, video, audio, subtitles, and final rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and produce character-consistent animated shorts across multiple shots with the dLazy storyboard service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files are sent to the third-party dLazy cloud service.

Mitigation: Send only content approved for that service and review files before attaching them.

Risk: Persistent CLI login stores an API key locally, which is a concern on shared or temporary machines.

Mitigation: Use per-run DLAZY_API_KEY authentication where safer, and rotate or revoke a key if exposure is suspected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Media assets]

**Output Format:** [Streaming text responses and generated storyboard project assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Projects can include scripts, reference images, shot videos, audio, subtitles, and a rendered short.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
