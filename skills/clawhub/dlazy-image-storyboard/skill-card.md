## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to turn briefs for film, advertising, short video, educational, or comic-style narratives into planned storyboard scripts, character references, and gated image-generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses dLazy's npm CLI and stores a dLazy API key locally.

Mitigation: Confirm trust in the CLI before installation, prefer npx for non-persistent use, and rotate or revoke the API key from the dLazy dashboard when it is no longer needed.

Risk: Storyboard prompts and referenced media files may be sent to dLazy cloud endpoints for generation.

Mitigation: Avoid sending sensitive prompts or media unless cloud processing by dLazy is acceptable for the project.

Risk: Generating images before the creative plan is confirmed could produce incorrect or unwanted outputs.

Mitigation: Follow the skill's confirmation gates for requirements, character design, script approval, and one-at-a-time generation.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with storyboard plans, prompts, confirmation gates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs hosted by dLazy after user-confirmed CLI execution.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
