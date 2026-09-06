## Description:

Image super-resolution tool for enhancing image clarity and details and returning an enhanced URL for low-resolution asset restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upscale low-resolution images through the dLazy hosted service and receive an enhanced image URL or saved output file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or local files explicitly provided to the skill may be uploaded to dLazy, and generated results are hosted by dLazy.

Mitigation: Only pass images approved for the dLazy cloud service, review output URLs before sharing, and use --dry-run when checking payloads and cost before an API call.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication when local storage is not desired, and rotate or revoke organization keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy service website](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Configuration instructions]

**Output Format:** [JSON response containing generated image metadata and URL; optional saved image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication; supports asynchronous task IDs with polling.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
