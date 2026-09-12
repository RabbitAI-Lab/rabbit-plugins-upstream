## Description:

amis-helper helps agents generate hand-written Baidu amis 6.x JSON Schema for CRUD admin pages, dialogs, forms, imports and exports, data-source adapters, refresh behavior, reusable examples, and delivery self-checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthoyx](https://clawhub.ai/user/anthoyx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to draft and review amis 6.x admin-page JSON for CRUD lists, add/edit/delete/import/export dialogs, validation, dictionary selects, remote autocomplete, data adapters, and component refresh flows. It is scoped to hand-authored or generated amis JSON Schema, not amis-editor visual configurations, mobile H5, SSR, or older amis versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated add/edit/delete/import/export JSON may be used in a real admin system with incorrect workflow behavior if it is not reviewed.

Mitigation: Review the generated JSON against the bundled self-check list and test it in the target amis 6.x environment before production use.

Risk: The documented rules are scoped to amis 6.x and tested mainly on amis 6.13.0; behavior may differ in amis-editor, mobile H5, SSR, amis 2.x, or early amis 3.x.

Mitigation: Apply the skill only within its documented scope, and verify version-specific behavior when the target environment differs from amis 6.13.0.

Risk: Backend business failures can be treated as successful submissions if non-standard responses are not adapted to amis status semantics.

Mitigation: Use the documented adaptor patterns for non-standard responses and test failure paths before relying on generated submit or refresh flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anthoyx/skills/amis-helper)
- [Skill definition](artifact/SKILL.md)
- [Metadata and scope](artifact/META.md)
- [Examples index](artifact/examples/INDEX.md)
- [CRUD guidance](artifact/references/crud.md)
- [Dialog and action guidance](artifact/references/dialog-actions.md)
- [Form controls guidance](artifact/references/form-controls.md)
- [API and data-source guidance](artifact/references/data-source.md)
- [Troubleshooting guide](artifact/references/pitfalls.md)
- [Configuration self-check](artifact/references/self-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with amis JSON snippets and complete JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces amis 6.x JSON Schema guidance for admin CRUD pages; generated JSON should be reviewed before use in a real admin system.]

## Skill Version(s):

1.2.10 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
