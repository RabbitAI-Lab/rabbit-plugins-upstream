## Description:

Helps agents generate videos from text prompts or images using Google Veo 3.1 through dLazy's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or extend videos from prompts and supplied media via dLazy's Veo 3.1 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to dLazy's cloud service.

Mitigation: Check media and prompts for sensitive content before submitting them to dLazy.

Risk: Video generation may consume paid credits.

Mitigation: Review the provider and model, and use the documented dry-run cost estimate before generating.

Risk: The CLI may save an API key locally.

Mitigation: Use the documented per-invocation environment variable option if persistent key storage is unsuitable.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands; the CLI returns JSON with generated asset URLs or asynchronous task IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, image references, video extension, and optional local download.]

## Skill Version(s):

1.3.26 (source: server-resolved release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
