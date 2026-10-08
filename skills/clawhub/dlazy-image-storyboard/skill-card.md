## Description:

Guides film, advertising, short-video, and educational storyboard creation through a plan-first workflow with approval gates before image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan character designs, write shot-by-shot scripts, generate storyboard images after approval, and prepare cinematic or narrative layouts for delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted services.

Mitigation: Review content before submission and avoid sharing sensitive prompts or media without authorization.

Risk: Using the CLI requires a dLazy API key stored locally or provided by environment variable.

Mitigation: Protect the key, use only a trusted installation, and rotate or revoke it if exposed.

Risk: One documentation line names a different CLI version than the pinned install commands.

Mitigation: Confirm the intended CLI version before installing; use the on-demand npx command if a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI repository (listed by skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Images, PDF]

**Output Format:** [Bulleted storyboard plans and scripts, image links, and a print-ready A4 storyboard layout]

**Output Parameters:** [1D text with linked image outputs; A4 landscape for final layout]

**Other Properties Related to Output:** [The workflow requests approval at requirements, character, script, and image-delivery gates.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
