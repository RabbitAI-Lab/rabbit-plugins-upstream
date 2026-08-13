## Description:

Creates code-driven motion graphics, kinetic typography, animated text videos, animated infographics, and explainer animations using Remotion-oriented workflows rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to start or continue dLazy motion-graphics projects through the dLazy CLI, including projects that use text, shapes, data, logos, and transitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, project context, and files attached with --files are sent to dLazy services.

Mitigation: Review the content before sending it and avoid attaching sensitive or restricted files unless that use is approved.

Risk: The dLazy API key is a credential saved in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Protect the key like other service credentials and rotate or revoke it from the dLazy dashboard when needed.

Risk: The skill installs or runs a third-party npm CLI.

Mitigation: Review the dLazy CLI package and prefer the pinned install or npx command shown in the artifact.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dLazy CLI and an API key; prompts and attached files may be sent to dLazy API and file-storage endpoints.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
