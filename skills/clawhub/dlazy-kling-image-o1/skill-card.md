## Description:

Generates images with Kling o1 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Kling o1 through the dLazy CLI, including text-to-image and image-to-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local images may be sent to dLazy's cloud service.

Mitigation: Review prompt text and input images before use, and avoid submitting sensitive material unless the user's policy allows it.

Risk: API credentials may be stored locally for the dLazy CLI.

Mitigation: Use OS user protections for the config file, prefer per-invocation environment variables when appropriate, and rotate or revoke exposed keys.

Risk: Non-dry-run generation calls may consume dLazy credits.

Mitigation: Use dry-run mode for cost checks when available and confirm paid usage before running generation requests.

Risk: Generated outputs are hosted by dLazy unless saved locally.

Mitigation: Treat hosted output URLs according to the user's data handling policy and save files locally when persistent control is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions]

**Output Format:** [JSON response with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs when --no-wait is used; generated images are hosted by dLazy unless saved locally.]

## Skill Version(s):

1.3.9 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
