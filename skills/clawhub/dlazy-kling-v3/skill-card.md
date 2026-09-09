## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short Kling v3 videos from text prompts or image references through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths provided to the skill may be uploaded to dLazy-hosted services.

Mitigation: Use the skill only with content approved for dLazy cloud processing and avoid sending sensitive files or prompts.

Risk: The dLazy API key can be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use scoped credentials where possible, keep the local config protected, and rotate or revoke the key if exposure is suspected.

Risk: The skill installs or runs the third-party @dlazy/cli npm package.

Mitigation: Install only if the publisher and package are trusted, and prefer the pinned package version declared by the artifact.

Risk: Video generation may consume account credits.

Mitigation: Use dry-run or cost-estimate behavior where appropriate and monitor organization credit balance before large generation runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing generated media URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated media to a local path when the CLI save option is used.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
