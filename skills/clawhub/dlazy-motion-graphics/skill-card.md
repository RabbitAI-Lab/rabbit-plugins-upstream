## Description:

Motion graphics, kinetic typography, animated text video, animated infographic, and explainer animation skill for creating code-driven animated graphics with Remotion code rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and agents use this skill to start or continue dLazy Motion Graphics projects for animated text, infographics, logo and shape animation, transitions, and explainer-style videos. It is best suited to code-driven Remotion graphics workflows rather than generative video footage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy CLI and SaaS endpoints, so prompts and selected parameters are sent to dLazy for processing.

Mitigation: Review the linked CLI source and service terms before use, and use the pinned npx invocation if you do not want to keep a global executable installed.

Risk: Attached local files are uploaded to dLazy media storage when passed through the CLI.

Mitigation: Attach only files that are appropriate to share with dLazy and avoid including secrets, private customer data, or regulated content unless approved for that service.

Risk: The workflow requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Protect the API key as a credential and rotate or revoke it from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and code-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project IDs and CLI authentication state; attached local files are uploaded through the dLazy CLI when used.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
