## Description:

Generates images from text prompts or reference images using Vidu Q2 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users create images from text prompts or reference images with Vidu Q2, including control over aspect ratio and resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local images are sent to dLazy's hosted service.

Mitigation: Use only prompts and images you are comfortable sharing with dLazy.

Risk: Login may save an API key locally.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if local persistence is undesirable.

Risk: Global installation runs the pinned third-party CLI package.

Mitigation: Review the pinned CLI package before installation, or use the npx option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image URLs, Shell commands, Guidance]

**Output Format:** [JSON image results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID or save the generated image locally.]

## Skill Version(s):

1.3.30 (source: ClawHub release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
