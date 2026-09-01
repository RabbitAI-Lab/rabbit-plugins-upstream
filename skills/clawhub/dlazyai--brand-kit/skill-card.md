## Description:

Brand Kit helps ecommerce teams keep generated product imagery consistent across SKUs by using a reusable brand.yaml for model, lighting, composition, spacing, and copy-tone constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, and developers use this skill to define one reusable visual brand kit and apply it across product-image generation workflows. It is suited to batch SKU imagery where model identity, color temperature, composition, whitespace, and style constraints need to remain consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to cloud image-generation providers during generation workflows.

Mitigation: Choose the provider intentionally, review brand.yaml before batch runs, and avoid submitting sensitive or unapproved source images.

Risk: Face reference images can be reused across many generated outputs and may create consent, rights, or likeness concerns.

Mitigation: Use face references only when the user has appropriate rights and consent for repeated commercial use.

Risk: Default demographic or styling fields in example brand files may unintentionally carry into production prompts.

Mitigation: Remove or replace demographic defaults and example styling before using the brand kit for a real store.

## Reference(s):

- [brand.yaml Field Reference](references/brand-schema.md)
- [Provider CLI Reference](references/provider-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update brand.yaml and may emit appended prompt text, dry-run reports, provider JSON summaries, or saved output paths when generation commands are run.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
