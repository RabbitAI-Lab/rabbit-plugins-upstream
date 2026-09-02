## Description:

Creates code-driven motion graphics, kinetic typography, animated infographics, and explainer animations using Remotion-style text, shapes, data, logos, and transitions rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to run dLazy's hosted motion-graphics agent for Remotion-style animated text, graphics, data, logos, transitions, and explainer video work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be sent to dLazy's hosted service.

Mitigation: Install only if that data flow is acceptable for the intended use, and avoid attaching sensitive files unless approved.

Risk: Authentication stores an organization-scoped dLazy API key in local CLI configuration.

Mitigation: Use OS account protections for the config file and rotate or revoke the key from the dLazy dashboard when needed.

Risk: The skill relies on a pinned npm CLI package to perform hosted API calls and optional file uploads.

Mitigation: Review the pinned package and source links before installation in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Streaming CLI text with Markdown and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference project-scoped chat sessions and uploaded files handled by the dLazy CLI.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
