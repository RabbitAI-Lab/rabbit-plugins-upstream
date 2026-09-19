## Description:

Creates code-driven motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations with Remotion code rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to start or continue dLazy motion-graphics projects for code-driven animated graphics, kinetic typography, animated infographics, and explainer videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to dLazy services, and attached local files are uploaded to dLazy media storage.

Mitigation: Avoid attaching confidential files unless that upload is intended and acceptable for the user's organization.

Risk: The skill relies on a pinned third-party CLI and stores an API key in local user configuration.

Mitigation: Review the pinned @dlazy/cli package or source before sensitive use, prefer npx when avoiding a global install, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI with the motion-graphics template; attached files are uploaded to dLazy media storage when used.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
