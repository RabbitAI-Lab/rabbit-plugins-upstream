## Description:

Generates detailed vector-style graphics from text prompts using the dLazy-hosted Recraft V4 Pro Vector model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to generate detailed graphic assets and illustrations from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied files are sent to a third-party cloud service, and generated results are hosted there.

Mitigation: Avoid submitting sensitive prompts or files; review the service terms before using hosted results.

Risk: The third-party CLI can persist an API key locally during login.

Mitigation: Use a per-invocation DLAZY_API_KEY when local key persistence is undesirable; protect and rotate credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro-vector)
- [dLazy CLI repository (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image assets, Files]

**Output Format:** [JSON result with a hosted image URL; optional locally saved asset]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode returns a task ID for later polling.]

## Skill Version(s):

1.3.25 (source: server-resolved release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
