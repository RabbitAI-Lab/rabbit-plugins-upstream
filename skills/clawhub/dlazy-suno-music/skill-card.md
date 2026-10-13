## Description:

Helps agents generate music with or without vocals using inspiration or custom-lyrics modes through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request music with automatic or custom lyrics, with optional instrumental output, through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided media are sent to dLazy, which hosts generated outputs.

Mitigation: Review prompts and media for sensitive content before submission, and assess the service's handling of hosted results.

Risk: Login may store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: The skill installs an external CLI package, and its image/png response example appears inconsistent with music output.

Mitigation: Review the pinned CLI package before installation and verify the actual result format rather than relying on the example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI project (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is accessed via hosted result URLs; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.27 (source: server-resolved ClawHub release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
