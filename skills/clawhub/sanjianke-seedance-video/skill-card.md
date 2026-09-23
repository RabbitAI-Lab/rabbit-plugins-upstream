## Description:

This skill helps agents call the a7w Seedance 2.0 API to create and manage multimodal video-generation jobs, assets, and task status using the user's own API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2253128](https://clawhub.ai/user/2253128)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent users use this skill to configure an a7w API key, inspect the Seedance plugin schema, upload or manage media assets, submit Seedance 2.0 video-generation jobs, and query asynchronous task results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled client can send the user's API key to an overridden host through --host or A7W_HOST.

Mitigation: Use the default api.a7w.cn endpoint and set --host or A7W_HOST only when the destination is fully trusted.

Risk: The bundled client can operate across the broader a7w marketplace, not only Seedance video endpoints.

Mitigation: Restrict use to the documented seedance commands and review requested app/API names before execution.

Risk: Seedance task submission can spend the user's account points and duplicate submissions may create duplicate charges.

Mitigation: Use a controlled API key, monitor point usage, and query existing task status instead of resubmitting the same job.

Risk: Generated media may require separate content, copyright, and policy review.

Mitigation: Review generated outputs before publication and apply the user's normal content compliance process.

## Reference(s):

- [Getting Started](references/getting-started.md)
- [Seedance 2.0 Create Task API](references/api-create.md)
- [Seedance 2.0 Create Asset API](references/api-createAsset.md)
- [Seedance 2.0 Create Group API](references/api-createGroup.md)
- [Seedance 2.0 Get Asset API](references/api-getAsset.md)
- [Seedance 2.0 Update Asset API](references/api-updateAsset.md)
- [Seedance 2.0 Delete Asset API](references/api-deleteAsset.md)
- [Seedance 2.0 Query Task API](references/api-query.md)
- [ClawHub Skill Page](https://clawhub.ai/2253128/skills/sanjianke-seedance-video)
- [a7w Compute Marketplace](https://api.a7w.cn/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write returned JSON to a user-selected output file when the client is invoked with --out.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
