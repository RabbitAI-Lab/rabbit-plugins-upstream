## Description:

Helps agents generate and edit images with Vidu Q2 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image generation or image-to-image edits using Vidu Q2 via dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media paths supplied to the CLI are sent to dLazy's cloud service.

Mitigation: Review prompts and media before submission; avoid sending sensitive content without authorization.

Risk: Logging in can store a dLazy API key locally.

Mitigation: Protect local credentials and revoke or rotate the key in the dLazy dashboard if needed.

Risk: A global CLI installation persists on the machine.

Mitigation: Use the documented pinned npx invocation if a persistent global install is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated image URLs or save images locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.23 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
