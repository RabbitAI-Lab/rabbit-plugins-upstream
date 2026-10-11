## Description:

Helps an agent generate a short video from a first-frame image and a text prompt using Jimeng through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short Jimeng videos from a supplied first-frame image and prompt through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's hosted service.

Mitigation: Only submit media and prompts you are comfortable sharing with dLazy.

Risk: Authentication requires a dLazy API key that the CLI may save locally.

Mitigation: Keep the key private and rotate or revoke it if exposed; use per-invocation credentials when preferred.

Risk: The documented input flag and output type are inconsistent.

Mitigation: Check CLI help and confirm the output type before running a generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and links to generated assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a generated asset URL or an asynchronous task identifier; the skill's documented flag and example output disagree on the input flag and media type.]

## Skill Version(s):

1.3.27 (source: ClawHub release; bundled skill frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
