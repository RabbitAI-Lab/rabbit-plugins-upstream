## Description:

Creates code-driven motion graphics, kinetic typography, animated infographics, explainer animations, and related videos using Remotion-style text, shapes, data, logos, and transitions rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to delegate motion-graphics video creation tasks to the dLazy hosted sandbox agent through a pinned CLI workflow. It is intended for code-driven animated graphics, including text animation, infographics, logo animations, transitions, and explainer-style motion design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to the external dLazy API.

Mitigation: Use the skill only for content that can be shared with the dLazy hosted service.

Risk: Attached local files are uploaded to dLazy media storage before the hosted agent uses them.

Mitigation: Review files before attachment and avoid uploading confidential or restricted material.

Risk: The CLI may store an API key in local user configuration.

Mitigation: Prefer per-invocation credentials when needed and rotate or revoke organization API keys from the dLazy dashboard.

Risk: A persistent global CLI install can leave a local executable on the system.

Mitigation: Use the pinned npx command for one-off execution when a persistent install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI command examples and streamed text responses from the hosted dLazy agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated Remotion code and project state; attached local files are uploaded to dLazy media storage before use.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
