## Description:

Helps an agent generate images from text prompts with Jimeng through the dLazy CLI, with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to request Jimeng text-to-image generation, optionally providing reference images and saving the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local media may be sent to the dLazy hosted service.

Mitigation: Confirm the user wants to use dLazy and avoid sending sensitive content without approval.

Risk: Image generation may consume account credits.

Mitigation: Use the available dry-run cost estimate when appropriate and confirm before costly requests.

Risk: The CLI can save an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Installing a third-party npm CLI introduces package supply-chain exposure.

Mitigation: Review the pinned package source before installing in sensitive environments.

## Reference(s):

- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text guidance with CLI examples; the CLI returns JSON containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download of generated images; asynchronous jobs can return a task ID.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; supplied skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
