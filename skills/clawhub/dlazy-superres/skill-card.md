## Description:

Image super-resolution tool that enhances image clarity and detail and returns an enhanced image URL for low-resolution restoration and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to upscale low-resolution images through the dLazy CLI/API and receive hosted enhanced image URLs or saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates execution to the external @dlazy/cli npm package.

Mitigation: Review the npm package and linked project metadata before installation, and prefer the pinned version declared in release metadata.

Risk: Selected local image paths may be uploaded to dLazy and generated outputs may be hosted on dLazy file storage.

Mitigation: Use only images approved for cloud processing and avoid submitting confidential or regulated content unless dLazy's terms and controls meet the user's requirements.

Risk: The skill requires dLazy API authentication stored in local configuration or provided through an environment variable.

Mitigation: Store the API key with user-only permissions, rotate or revoke it from the dLazy dashboard when needed, and avoid exposing it in shared logs.

Risk: The artifact example uses --prompt while the documented super-resolution options use --image.

Mitigation: Run dlazy superres -h and use the documented --image option until the publisher corrects the documentation mismatch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI source link from release metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON command output containing hosted image URLs; optional downloaded image files via --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, dLazy API authentication, and an image URL or local image path.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
