## Description:

Brand Kit uses a reusable brand.yaml file to keep model identity, color temperature, composition, spacing, and copy tone consistent across ecommerce image-generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to create and apply a shared brand.yaml specification so batches of SKU images keep a consistent store identity, model appearance, lighting, framing, layout, and visual constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images can be sent to the selected image-generation provider when generation is invoked.

Mitigation: Install and run only when that data transfer is acceptable; use --dry-run or an explicit --provider to verify the request before sending it.

Risk: Example brand.yaml model identity fields or visual constraints may be reused without matching the user's intended store identity.

Mitigation: Review and edit brand.yaml before reuse, especially model identity, forbidden elements, platform compliance, and visual style fields.

## Reference(s):

- [brand.yaml Field Reference](references/brand-schema.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/brand-kit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with YAML configuration examples, inline shell commands, optional JSON reports, and generated image files when invoked through the generation helper.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brand constraints are appended to prompts selectively by task; --dry-run can show the outgoing request before provider invocation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
