## Description:

Turns an idea into a reviewable video-production plan, builds a canvas workflow for story, characters, scenes, shots and video assembly, and supports stepwise generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn an idea into a confirmed production plan and canvas workflow for generating and assembling a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI may save an API key on the local machine.

Mitigation: Review local credential storage before login and rotate or revoke the key if needed.

Risk: Prompts and selected media may be sent to dLazy servers.

Mitigation: Share only content you are comfortable sending to the service.

Risk: The workflow combines canvas planning with terminal-based generation commands.

Mitigation: Confirm each generation step, review commands before execution, and check the intended @dlazy/cli version before installing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source (tool reference; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown plan and status updates, canvas workflow configuration, and generation result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plan review precedes canvas application; generation steps require user confirmation.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
