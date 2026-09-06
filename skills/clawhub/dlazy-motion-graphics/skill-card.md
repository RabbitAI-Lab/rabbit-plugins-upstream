## Description:

Creates code-driven motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations using Remotion-style text, shapes, data, logos, and transitions rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to ask the dLazy motion-graphics agent for project-scoped help creating and refining code-driven animated graphics and explainer video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI that stores a dLazy API key locally.

Mitigation: Use the pinned npx invocation when avoiding a persistent global install, protect the local CLI configuration file, and rotate or revoke the API key from dLazy when needed.

Risk: Prompts and explicitly attached files are sent to dLazy services for processing.

Mitigation: Review prompts and attachments for sensitive data before invocation, and attach only files intended for upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI-generated responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project-scoped follow-up instructions; user-selected file attachments are uploaded by the dLazy CLI.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
