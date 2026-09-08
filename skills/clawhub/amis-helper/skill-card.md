## Description:

Generates Baidu amis 6.x low-code JSON Schema for hand-authored admin pages, including CRUD lists, dialogs, forms, import/export flows, response adaptation, component refresh behavior, reusable examples, and self-check guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthoyx](https://clawhub.ai/user/anthoyx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate and review amis 6.x JSON Schema for backend management pages, including CRUD tables, dialog-based add/edit/delete flows, form validation, remote selects, Excel import/export, API response adapters, and refresh wiring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on generic frontend, API, or form troubleshooting requests where amis is not actually in scope.

Mitigation: Invoke it for clearly amis-related tasks, or narrow the trigger matrix so generic frontend/API/form language does not route here.

Risk: Generated amis JSON may not match applications outside the documented amis 6.x, hand-authored admin-page scope.

Mitigation: Check the documented version and scope boundaries before use, and run the bundled self-check checklist before adopting generated configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anthoyx/skills/amis-helper)
- [amis-helper metadata](artifact/META.md)
- [CRUD rules](artifact/references/crud.md)
- [API and data source rules](artifact/references/data-source.md)
- [Dialog and action rules](artifact/references/dialog-actions.md)
- [Form control rules](artifact/references/form-controls.md)
- [Troubleshooting guide](artifact/references/pitfalls.md)
- [Self-check checklist](artifact/references/self-check.md)
- [Example index](artifact/examples/INDEX.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with amis JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing guidance and JSON configuration; no shell execution is expected.]

## Skill Version(s):

1.2.7 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
