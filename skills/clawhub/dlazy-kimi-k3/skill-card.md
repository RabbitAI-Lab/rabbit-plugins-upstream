## Description:

Uses the hosted Kimi K3 model for text generation and complex reasoning, with optional image and video understanding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request analysis, writing, or code from the hosted model and optionally provide images or videos for context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required third-party CLI stores a service API key locally.

Mitigation: Review the CLI before installation, use npx to avoid a global install if preferred, and rotate or revoke the key if needed.

Risk: Prompts and explicitly supplied media are sent to dLazy-hosted services.

Mitigation: Avoid sending sensitive prompts or files unless sharing them with the service is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of immediate content.]

## Skill Version(s):

1.2.21 (source: server release metadata; bundled skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
