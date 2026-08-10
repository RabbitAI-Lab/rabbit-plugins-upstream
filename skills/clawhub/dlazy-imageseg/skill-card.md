## Description:

Image matting tool that separates foreground from background and returns a transparent-background image URL for product image processing, people cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to remove image backgrounds through the dLazy CLI/API for product imagery, people cutouts, and image composition workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images passed to the command are processed by a third-party hosted service.

Mitigation: Use images appropriate for third-party processing and review data sensitivity before invocation.

Risk: The CLI can store a dLazy API key in a local user configuration file.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when persistent local credentials are not desired, and rotate or revoke keys when needed.

Risk: The workflow installs or runs a third-party npm CLI package.

Mitigation: Review the pinned package and source before installing in trusted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown instructions with bash examples; runtime CLI output is JSON containing generated image URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload user-selected images to dLazy-hosted endpoints for processing.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
