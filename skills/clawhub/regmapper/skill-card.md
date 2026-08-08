## Description:

Browse, search, and annotate regulations via the RegMapper API. Use when asked about regulations, rules, compliance requirements, project annotations, or comparing regulation versions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ogruenig](https://clawhub.ai/user/ogruenig)

### License/Terms of Use:

MIT-0

## Use Case:

Regulatory and compliance teams, legal researchers, and developers use this skill to search RegMapper regulations, inspect rule text, compare regulation versions, and manage project comments when they have appropriate project permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a RegMapper account token.

Mitigation: Install it only when agent access to the RegMapper account is acceptable, store REGMAPPER_API_TOKEN privately, and keep .env out of version control.

Risk: The skill can create or update project comments when the token has write access.

Mitigation: Review project permissions before write operations and only create or update comments for projects where the intended auth level is write.

## Reference(s):

- [RegMapper homepage](https://regmapper.net)
- [RegMapper API schema](https://www.regmapper.net/api/v1/schema/)
- [Bundled OpenAPI specification](artifact/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with API request examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RegMapper endpoint selections, token setup guidance, and project comment workflow guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
