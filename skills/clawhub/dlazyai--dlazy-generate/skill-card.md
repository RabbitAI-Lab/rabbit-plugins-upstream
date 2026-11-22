## Description:

A comprehensive generation skill that routes image, video, and audio requests to an appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can ask an agent to create or transform images, videos, or audio; the skill chooses a suitable dLazy CLI model and returns generated media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to invoke generation for requests that only discuss creating media.

Mitigation: Confirm the user wants media generated or transformed before running a CLI command.

Risk: The scanner could not resolve several references, leaving details about the pinned CLI package incompletely assessed.

Mitigation: Review the package and its linked source and confirm the pinned version before installing; use the documented npx option only if you trust the package.

Risk: Prompts and supplied local media are sent to dLazy hosted APIs and storage.

Mitigation: Avoid sending confidential prompts or files unless their use with the hosted service is authorized.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, JSON]

**Output Format:** [JSON result envelope with hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted on dLazy file storage.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
