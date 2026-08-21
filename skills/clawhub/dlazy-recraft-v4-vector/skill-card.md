## Description:

Invokes dLazy's hosted Recraft V4 Vector CLI flow for prompt-based logo, icon, and design-asset generation; server security evidence notes that the SVG/vector claim conflicts with documented PNG output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Recraft V4 Vector service from an agent workflow for prompt-based logo, icon, and design asset generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims SVG/vector output while documented successful responses show image/png URLs.

Mitigation: Validate returned assets before relying on them as true vector outputs; treat results as potentially raster PNG unless publisher documentation and enforcement are corrected.

Risk: Prompts and explicitly referenced local media files are sent to dLazy hosted endpoints, and the CLI stores a dLazy API key locally unless supplied per invocation.

Mitigation: Use the skill only with data suitable for a third-party hosted service, rotate or revoke API keys as needed, and prefer per-invocation credentials where local persistence is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response containing hosted image output URLs, plus agent-facing shell commands and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; synchronous calls may wait for completion, while --no-wait returns a generation task identifier.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
