## Description:

Query Mosqlimate dengue, zika, and chikungunya data, models, and forecasts, and validate or upload predictions with mosqlient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luabida](https://clawhub.ai/user/luabida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data scientists use this skill to query Brazilian arbovirus, climate, mosquito, vegetation, and model data, and to validate or upload forecasts to the Mosqlimate registry.

### Deployment Geography for Use:

Brazil

## Known Risks and Mitigations:

Risk: A forecast with incorrect dates, locations, or values could be written to the registry or made public.

Mitigation: Validate the forecast, review its parameters with the user, require explicit confirmation before upload, and publish only when explicitly requested.

Risk: API credentials could be exposed through logged or shared commands.

Mitigation: Keep the API key in the MOSQLIMATE_API_KEY environment variable and do not paste it into commands that are logged or shared.

Risk: An untrusted API endpoint or downloaded dependency could affect the execution environment.

Mitigation: Use trusted API endpoints and review the dependency installation before running the skill.

## Reference(s):

- [Datastore commands](references/datastore.md)
- [Registry commands](references/registry.md)
- [Prediction uploads](references/predictions.md)
- [Troubleshooting](references/troubleshooting.md)
- [Mosqlimate API documentation](https://api.mosqlimate.org/docs/)

## Skill Output:

**Output Type(s):** [JSON, CSV, Shell commands, Guidance]

**Output Format:** [JSON or CSV data, with shell commands and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results can be saved to a file; fields depend on the selected data or registry query.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
