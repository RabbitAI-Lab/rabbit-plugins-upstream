## Description:

Generate high-quality images with Doubao Seedream 4.5, supporting text-to-image and image-to-image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or transform images through the dLazy CLI using Doubao Seedream 4.5. It is intended for prompt-driven image generation workflows that may include local or URL-based reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud CLI that stores a dLazy API key and sends prompts or selected files to dLazy services.

Mitigation: Install only when comfortable using dLazy as the cloud provider, protect the API key, and rotate or revoke credentials when access is no longer needed.

Risk: Local files passed as image inputs may be uploaded to dLazy media storage for model processing.

Mitigation: Avoid passing private local files unless upload to dLazy is intended and appropriate for the user's data handling requirements.

Risk: The CLI can make paid API calls or upload files based on user-provided prompts and parameters.

Mitigation: Prefer dry runs or explicit confirmation before cost-incurring generation calls or file uploads.

Risk: A global npm install persists the dLazy CLI binary on the system.

Mitigation: Use the pinned npx invocation when a persistent global binary is not desired, and review the pinned package before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted file URLs and can be saved locally with the CLI.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
