## Description:

A structured workflow skill dedicated to social-media carousel design using a single-confirmation, cover-first process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan social-media carousel slides, confirm direction, generate a cover first, and then create the remaining slides with consistent visual structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run a third-party CLI.

Mitigation: Review the exact @dlazy/cli release before use and prefer npx or a contained environment over a global install.

Risk: Prompts and media may be sent to dLazy hosted services.

Mitigation: Only send content suitable for dLazy processing, and keep the dLazy API key scoped, revocable, and rotated when needed.

Risk: User-derived prompt text in shell commands can create execution-safety issues if concatenated unsafely.

Mitigation: Pass prompt content as structured CLI arguments or apply shell-specific escaping before command execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with confirmation tables, phase status, inline shell commands, and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation between major generation steps; uses dLazy CLI commands when image generation is approved.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
