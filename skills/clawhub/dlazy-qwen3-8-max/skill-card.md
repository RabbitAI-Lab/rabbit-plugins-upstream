## Description:

Uses dLazy's Qwen 3.8 Max service for text- and image-prompted reasoning, coding, and long-context analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users invoke the dLazy CLI to generate text, code, and analysis from prompts and optional images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to dLazy's hosted service.

Mitigation: Send only content approved for that service and review media paths before invoking the skill.

Risk: The CLI requires an API key and may store it locally.

Mitigation: Use per-run DLAZY_API_KEY when local key storage is undesirable; review the pinned npm package before installation.

## Reference(s):

- [dLazy CLI source (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON-wrapped generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of immediate content.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
