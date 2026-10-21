## Description:

Helps agents generate transition videos from a first and last frame using the dLazy Jimeng CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to instruct an agent to generate a transition video between supplied first and last frame images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are transmitted to the third-party dLazy service, which hosts generated outputs.

Mitigation: Review media and prompts for sensitive content before submission and check the service terms before use.

Risk: The skill requires a third-party npm CLI, and login may save an API key locally.

Mitigation: Review the CLI before installation; use the pinned npx invocation for one-off use and safeguard locally stored credentials.

Risk: Example commands use an image flag that conflicts with the documented first- and last-frame options.

Mitigation: Check the CLI help for the correct flags before running a generation request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package linked in skill metadata](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown instructions and CLI commands; CLI results are JSON with hosted media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return an asynchronous task ID or save generated media to a local path.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; source file frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
