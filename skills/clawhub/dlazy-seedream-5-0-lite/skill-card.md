## Description:

Generates images with Doubao Seedream 5.0 Lite from text prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images through dLazy's hosted Seedream 5.0 Lite service from prompts, reference images, and size or resolution settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image paths may be uploaded to dLazy's hosted service.

Mitigation: Avoid sending confidential prompts or sensitive local files unless they are approved for the dLazy service.

Risk: API usage may consume dLazy credits.

Mitigation: Use dry-run or review cost estimates before making generation calls when budget impact matters.

Risk: Login stores an API key in local CLI configuration.

Mitigation: Protect the user configuration file, prefer per-invocation environment variables where appropriate, and rotate or revoke the key from the dashboard if exposed.

Risk: Broad trigger phrases may invoke the skill when the user did not intend to use dLazy or Seedream.

Mitigation: Invoke the skill only for explicit dLazy or Seedream image-generation requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [JSON responses containing generated image URLs, plus Markdown guidance and shell commands for setup or error handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation may return hosted file URLs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.6 (source: release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
