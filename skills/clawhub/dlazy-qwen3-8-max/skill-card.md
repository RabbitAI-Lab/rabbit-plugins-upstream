## Description:

Uses the dLazy CLI to request Qwen 3.8 Max responses to text prompts and optional image inputs for reasoning, coding, and long-context analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can request hosted Qwen responses for complex reasoning, code work, and analysis of text or supplied images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and supplied media are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive content unless its transmission to dLazy is approved.

Risk: The third-party npm CLI is required to run the skill.

Mitigation: Review the pinned CLI package and its source before installing in sensitive environments.

Risk: CLI login saves an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent local storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen3-8-max)
- [dLazy CLI source (linked in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Model-generated responses returned in a JSON CLI result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous generation returns a task ID for later polling.]

## Skill Version(s):

1.2.23 (source: ClawHub release metadata; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
