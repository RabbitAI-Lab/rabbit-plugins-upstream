## Description:

Generates Jimeng image-to-video outputs from a first-frame image and prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos from a supplied first-frame image and prompt through the dLazy/Jimeng service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy/Jimeng cloud endpoints for generation.

Mitigation: Use only prompts and media approved for that service, and avoid sensitive content unless the applicable service terms and data-handling requirements allow it.

Risk: The saved API key may not be protected as strongly as the skill claims.

Mitigation: Prefer supplying DLAZY_API_KEY per invocation, or verify that ~/.dlazy/config.json is readable only by the current OS user after login.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an async task ID; --save can download generated media to a local path.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
