## Description:

amis-helper helps agents generate Baidu AMIS JSON Schema for CRUD pages, dialogs, forms, imports, and exports using reusable patterns and known pitfall checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthoyx](https://clawhub.ai/user/anthoyx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft production-oriented AMIS page schemas and avoid common configuration mistakes in CRUD tables, dialogs, forms, file import/export flows, and remote data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CRUD, delete, import, export, or bulk-bind actions could target unintended application APIs if placeholders are reused without review.

Mitigation: Review generated actions before use and replace placeholder endpoints only with intended application APIs.

Risk: AMIS configuration mistakes can lead to failed reloads, stuck loading states, invalid autocomplete behavior, or broken file transfer flows.

Mitigation: Check generated schemas against the bundled CRUD, dialog-action, form-control, data-source, and pitfalls references before deployment.

## Reference(s):

- [CRUD guidance](references/crud.md)
- [API and data source guidance](references/data-source.md)
- [Dialog and action-chain guidance](references/dialog-actions.md)
- [Form controls guidance](references/form-controls.md)
- [Pitfalls checklist](references/pitfalls.md)
- [Server-resolved source provenance](https://github.com/AnthoyX/skill-dev/tree/main/amis-helper)
- [ClawHub skill page](https://clawhub.ai/anthoyx/skills/amis-helper)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs commonly include AMIS JSON Schema fragments for CRUD pages, dialogs, forms, imports, exports, and data-source adapters.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
