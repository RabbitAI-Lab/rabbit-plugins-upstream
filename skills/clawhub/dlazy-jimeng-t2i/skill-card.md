## Description:

Helps agents generate images from text prompts using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text prompts and optional reference images into generated images with Jimeng via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's cloud service.

Mitigation: Avoid sending sensitive prompts or files unless their use with dLazy is approved.

Risk: Login can save a dLazy API key locally, and global installation leaves a CLI installed.

Mitigation: Protect local credentials and use the pinned npx option when a global CLI install is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI repository (skill metadata link; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Image files]

**Output Format:** [Text guidance and CLI commands; JSON results with image URLs or optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID instead of immediate image URLs.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
