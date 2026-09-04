## Description:

Generates Baidu amis low-code JSON Schema configurations with reusable CRUD, dialog, form, import, and export patterns plus documented pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthoyx](https://clawhub.ai/user/anthoyx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Baidu amis 6.x admin pages use this skill to draft and review hand-written JSON Schema configurations for CRUD pages, dialogs, forms, imports, exports, and data-source adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated amis schemas can affect real business data when connected to delete, import, download, or backend API endpoints.

Mitigation: Review generated JSON and endpoint bindings before use, especially for destructive actions and file workflows.

Risk: The guidance is scoped to hand-written amis 6.x JSON Schema patterns and was validated primarily against amis 6.13.0.

Mitigation: Confirm the target runtime is amis 6.x and run the bundled self-check before deployment; adjust separately for amis-editor, mobile H5, SSR, or older amis versions.

## Reference(s):

- [CRUD specifications](references/crud.md)
- [Dialog and action-chain specifications](references/dialog-actions.md)
- [Form control specifications](references/form-controls.md)
- [API and data-source specifications](references/data-source.md)
- [Pitfalls guide](references/pitfalls.md)
- [Generated configuration self-check](references/self-check.md)
- [Examples index](examples/INDEX.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated amis JSON Schema configurations should be reviewed and adapted to the user's backend APIs before use.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
