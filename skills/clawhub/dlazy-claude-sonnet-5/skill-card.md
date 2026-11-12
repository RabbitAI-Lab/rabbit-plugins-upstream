## Description:

Provides access to Claude Sonnet 5 for reasoning, code generation, long-horizon agent tasks, and prompts with text, image, or video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate text and code or handle complex tool-oriented tasks through dLazy's Claude Sonnet 5 service. Prompts can include text, images, or videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image or video files are sent to dLazy hosted services for processing.

Mitigation: Avoid sending sensitive content unless the service is approved for that data.

Risk: The security scan had medium confidence: skill analysis was partial, some local references were missing, and the external CLI package was not inspected. The scan also notes that the CLI setup does not clearly match the advertised model capabilities.

Mitigation: Review the pinned CLI package and confirm its authentication and API behavior match expectations before use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [npm package listed in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Guidance]

**Output Format:** [JSON response envelope containing generated model output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID; generated assets can be saved to a local file.]

## Skill Version(s):

1.2.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
