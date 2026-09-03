## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to authenticate with dLazy and run image vectorization jobs that convert selected raster image inputs into hosted vectorized outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and related parameters are sent to dLazy hosted endpoints.

Mitigation: Use only inputs appropriate for dLazy processing and review organizational data-sharing requirements before invoking the skill.

Risk: A dLazy API key may be stored in local CLI configuration.

Mitigation: Prefer per-invocation environment variables or on-demand npx usage on shared machines, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact examples conflict about whether vectorization should use --image or --prompt.

Mitigation: Verify the current command syntax with dlazy vectorize -h before execution and prefer the documented image input option.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs or an asynchronous task identifier depending on CLI flags.]

## Skill Version(s):

1.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
