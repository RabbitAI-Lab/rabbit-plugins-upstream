## Description:

Helps agents generate and edit images from prompts and up to five reference images through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request everyday image generation and edits, optionally providing reference images and choosing an aspect ratio or quality level.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to the third-party dLazy hosted service.

Mitigation: Review sensitive prompts and files before use, and check the pinned CLI package and source before installing.

Risk: Login may store a dLazy API key on the local machine.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with CLI commands and image-result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with hosted image URLs; results can optionally be saved locally.]

## Skill Version(s):

1.2.18 (source: ClawHub release metadata; skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
