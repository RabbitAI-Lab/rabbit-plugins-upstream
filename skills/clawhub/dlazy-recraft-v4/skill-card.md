## Description:

Generates 1MP raster images with Recraft V4 through the dLazy CLI for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to generate Recraft V4 raster images through the dLazy CLI, returning hosted image results or optionally saving generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files passed to the tool are uploaded to dLazy's hosted service.

Mitigation: Avoid sending sensitive inputs unless approved for dLazy processing, and review organization policy before use.

Risk: Authentication may persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global installation adds a persistent third-party CLI binary to the environment.

Mitigation: Prefer the pinned npx invocation or verify the pinned dLazy CLI package before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files]

**Output Format:** [JSON result with generated image URLs and optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication; async mode may return a generation task for later polling.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
