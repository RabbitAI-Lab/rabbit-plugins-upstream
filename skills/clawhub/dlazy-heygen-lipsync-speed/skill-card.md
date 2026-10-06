## Description:

Helps agents generate lip-synced video quickly from video and audio inputs using dLazy's HeyGen Lipsync Speed service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn video and audio inputs into lip-synced video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media supplied to the CLI may be uploaded to dLazy, and generated results are hosted by dLazy.

Mitigation: Only submit media approved for cloud processing and review dLazy's service terms before use.

Risk: Authentication can store an API key locally.

Mitigation: Protect local CLI credentials and avoid sharing API keys in prompts or logs.

Risk: Published examples contain parameter and output mistakes that may cause failed or misleading runs.

Mitigation: Check the installed command's help and verify the returned output before relying on it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a hosted result URL or a saved file path after generation.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
