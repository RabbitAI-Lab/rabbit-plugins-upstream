## Description:

A workflow skill for designing marketing brochures, from requirements gathering and layout planning through confirmed mock-up delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, design, and business users use this skill to plan brochure content, generate layout-first image prompts, and produce folded or lifestyle mock-ups after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on a third-party npm CLI and cloud service that can receive prompts and uploaded media.

Mitigation: Review the dLazy CLI before use, prefer the npx option for less persistent execution, and only provide brochure text or media intended for that service.

Risk: The CLI stores API credentials in a local configuration file unless an environment variable is used.

Mitigation: Use least-privilege API keys, rotate or revoke keys when needed, and prefer per-session DLAZY_API_KEY use where persistent local credentials are not desired.

Risk: Shell-built prompts containing quotes or metacharacters can be fragile when passed to CLI commands.

Mitigation: Review generated commands before execution and avoid including untrusted or unsanitized prompt text in shell invocations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates staged brochure layout generation, confirmation gates, and mock-up delivery through the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
