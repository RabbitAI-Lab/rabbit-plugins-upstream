## Description:

Text-to-vector skill for creating logo, icon, and scalable design assets from prompts using the dLazy Recraft V4 Vector CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external agents use this skill to request prompt-based graphic generation for logos, icons, and other reusable design assets through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is described as SVG/vector generation, but the artifact output example documents PNG results.

Mitigation: Confirm the actual returned asset type before relying on the skill for editable vector workflows.

Risk: The skill installs and invokes a third-party CLI that sends prompts and supplied media paths to dLazy-hosted services.

Mitigation: Use npx or a sandbox where practical, avoid elevated shells, and only provide credentials and input files appropriate for the dLazy service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a hosted dLazy generation API and may return generated asset URLs or asynchronous task identifiers.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
