## Description:

Generates 1MP raster images with Recraft V4 through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill to generate raster images from prompts, choose aspect ratios, run dry runs, and save generated assets through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly provided files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only with content approved for dLazy's service and avoid submitting sensitive files unless permitted by applicable policy.

Risk: Authentication uses a dLazy API key that may be saved in the local CLI configuration.

Mitigation: Prefer npx or DLAZY_API_KEY for ephemeral use when appropriate, protect the local config, and rotate or revoke the key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses containing generated image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned @dlazy/cli version and can return asynchronous task IDs when --no-wait is used.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
