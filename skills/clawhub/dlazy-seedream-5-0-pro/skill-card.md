## Description:

Helps agents generate detailed images, typography-rich compositions, and brand visuals with Seedream 5.0 Pro through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and design teams use this skill to request commercial key visuals and brand assets from text prompts, with optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the third-party dLazy CLI executes external software.

Mitigation: Confirm that you trust the dLazy CLI before installing it; use the pinned npx invocation to avoid a persistent global install.

Risk: Prompts and any local media files supplied to the CLI are sent to dLazy services.

Mitigation: Avoid sending sensitive prompts or files unless you are comfortable sharing them with dLazy.

Risk: An exposed dLazy API key could permit unauthorized use.

Mitigation: Rotate or revoke the API key through the dLazy dashboard if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation results provide image URLs; an optional save command downloads the image locally.]

## Skill Version(s):

1.2.27 (source: ClawHub release metadata; skill instructions pin dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
