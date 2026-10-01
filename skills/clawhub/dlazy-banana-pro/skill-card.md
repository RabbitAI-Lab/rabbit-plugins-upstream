## Description:

Guides agents to generate and edit images with Nano Banana Pro using text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to generate or edit images from prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local images are sent to the dLazy cloud service.

Mitigation: Avoid private prompts or files unless you intend to share them with the service.

Risk: Generation can consume paid credits.

Mitigation: Use dry-run to estimate cost before making requests.

Risk: A third-party CLI handles requests and stores an API key when logging in.

Mitigation: Review the package before installing, prefer on-demand use if appropriate, and revoke the key when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results can include generated image URLs or an asynchronous task ID; images can optionally be saved locally.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata; artifact frontmatter states 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
