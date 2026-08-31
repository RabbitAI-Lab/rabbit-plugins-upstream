## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals, educators, marketers, and agent developers use this skill to turn creative briefs into structured storyboard plans, character references, panel prompts, and rendered image-delivery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a dLazy API key and may store it in local CLI configuration.

Mitigation: Install only if the publisher and npm package are trusted; use DLAZY_API_KEY for per-run authentication when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts, parameters, and user-supplied media can be sent to dLazy-hosted API and media services.

Mitigation: Only provide media files intended for upload to dLazy services, and review generated media URLs before sharing them outside the intended workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured storyboard prompts, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; user-supplied media may be uploaded to dLazy-hosted services for generation.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
