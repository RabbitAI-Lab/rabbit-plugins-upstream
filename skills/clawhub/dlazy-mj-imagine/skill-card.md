## Description:

Helps agents request stylized image generation with selectable aspect ratio, bot type, and grid or U1–U4 output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative professionals and developers use this skill to generate stylized images through the dLazy service, choosing aspect ratio, bot type, and an image from the output grid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy, and generated images are hosted by dLazy.

Mitigation: Only submit content you are comfortable sharing with the hosted service.

Risk: Authentication stores an API key locally when using the CLI login or auth command.

Mitigation: Protect the local key and rotate or revoke it from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image links]

**Output Format:** [Text with shell commands and JSON image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved to a local path.]

## Skill Version(s):

1.3.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
