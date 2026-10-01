## Description:

Helps create and refine code-driven motion graphics, kinetic typography, and animated infographics using Remotion rather than AI-generated footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to build and revise project-based animated text, graphics, data visualizations, and explainer videos through the dLazy motion-graphics assistant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files may be sent to dLazy's external service.

Mitigation: Use the service only when appropriate for the data; review attachments before uploading.

Risk: Login stores a revocable API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if compromised.

Risk: Using --clear drops saved project session context.

Mitigation: Confirm the project and preserve needed context before clearing its session.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-motion-graphics)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Streamed text and Remotion code through CLI chat]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up turns; motion-graphics video can be polished and exported.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; supplied skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
