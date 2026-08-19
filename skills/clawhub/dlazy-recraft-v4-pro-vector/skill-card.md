## Description:

Generates high-fidelity vector-style image assets with Recraft V4 Pro Vector for production-grade SVG assets and detailed illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to call the dLazy hosted Recraft V4 Pro Vector service from the CLI and generate production-oriented vector-style image assets from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected local files may be uploaded to the dLazy cloud service for generation.

Mitigation: Confirm the user is comfortable sharing the prompt and any selected files with dLazy before invoking the CLI; avoid sending sensitive files unless approved.

Risk: Generated outputs are hosted remotely by dLazy.

Mitigation: Treat returned output URLs as externally hosted artifacts and avoid assuming they are private or local-only.

Risk: Authentication can persist an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY or npx when less local persistence is preferred, and rotate or revoke organization keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files]

**Output Format:** [JSON result containing generated output metadata and hosted file URLs, or async task status when no-wait mode is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports prompt, aspect ratio, dry-run, async generation, and timeout options.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
