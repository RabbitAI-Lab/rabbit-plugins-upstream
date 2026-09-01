## Description:

Generates Baidu amis low-code JSON Schema for CRUD, dialog, form, import, and export admin-page configurations, with reusable skeletons and rules for avoiding common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthoyx](https://clawhub.ai/user/anthoyx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate and review hand-written Baidu amis 6.x JSON Schema for backend admin CRUD pages. It helps assemble list pages, dialogs, form controls, upload/download flows, data-source adaptors, and self-checks before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated admin UI configurations may call authenticated CRUD, upload, download, and delete endpoints.

Mitigation: Review generated JSON before deployment, especially destructive or bulk actions, and replace placeholder URLs with appropriately scoped backend routes.

Risk: The skill is scoped to hand-written Baidu amis 6.x JSON Schema and excludes amis-editor output, mobile H5, and SSR scenarios.

Mitigation: Use the skill only for matching amis 6.x admin-page configuration work and verify outputs against the included self-check checklist.

Risk: Some rules are based on practical observations rather than independent local verification for every amis version.

Mitigation: Check the rule confidence metadata and retest behavior in the target amis runtime when adopting rules outside the documented 6.13.0 baseline.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anthoyx/skills/amis-helper)
- [META.md](META.md)
- [CRUD rules](references/crud.md)
- [Dialog and action rules](references/dialog-actions.md)
- [Form control rules](references/form-controls.md)
- [API and data-source rules](references/data-source.md)
- [Pitfall index](references/pitfalls.md)
- [Self-check checklist](references/self-check.md)
- [Example index](examples/INDEX.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and complete JSON example files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for hand-written Baidu amis 6.x JSON Schema; generated configurations should be reviewed and placeholder API routes replaced before deployment.]

## Skill Version(s):

1.2.0 (source: frontmatter, server release, CHANGELOG released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
