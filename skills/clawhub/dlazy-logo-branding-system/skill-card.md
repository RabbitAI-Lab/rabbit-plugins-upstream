## Description:

A professional pipeline for building everything from a core mark to a complete brand visual system, ensuring creative quality, execution consistency, and shippable delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, brand teams, and developers use this skill to plan and execute a staged logo and brand identity workflow, from requirements gathering through core mark concepts and downstream brand applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on installing or invoking the external @dlazy/cli npm package.

Mitigation: Review the package source and prefer npx or a contained environment when a persistent global install is not desired.

Risk: Prompts and selected local media may be sent to dLazy services for generation and hosted result delivery.

Mitigation: Use the skill only with content appropriate for dLazy services and avoid submitting sensitive local media unless approved.

Risk: The dLazy API key may be stored in local CLI configuration or provided through an environment variable.

Mitigation: Use trusted environments for authentication and rotate or revoke the API key when working on shared or untrusted systems.

Risk: Server release metadata and artifact frontmatter report different skill versions.

Mitigation: Use the server release version for this card and verify pinned CLI/package versions before deployment.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with requirements summaries, design plans, prompt drafts, command snippets, todo status, and generated result URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses staged user confirmation before generation and depends on the dLazy CLI plus a dLazy API key.]

## Skill Version(s):

1.2.13 (source: server release metadata; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
