## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan-first, render-later workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams, marketers, educators, and agents use this skill to turn briefs into cinematic or narrative storyboard plans, image-generation prompts, and final storyboard delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Third-party CLI installation and execution can add persistent tooling to the user's system.

Mitigation: Prefer the documented npx invocation when persistent global installation is not needed, and review generated commands before execution.

Risk: The workflow can upload prompts and local media files to dLazy services for generation.

Mitigation: Avoid passing sensitive local files unless required, and confirm that shared prompts and assets are appropriate for cloud processing.

Risk: API keys may remain in local CLI configuration after use.

Mitigation: Rotate or revoke the dLazy API key when the skill is no longer used or if credential exposure is suspected.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with storyboard planning bullets, prompt drafts, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs through the dLazy CLI after user confirmation.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
