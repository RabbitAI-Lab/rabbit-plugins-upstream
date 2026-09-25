## Description:

Generates OpenAPI/Swagger API documentation from code by analyzing function and method signatures, parameters, and return types.

This skill is ready for commercial/non-commercial use.

## Publisher:

[honestqiao](https://clawhub.ai/user/honestqiao)

### License/Terms of Use:


## Use Case:

Developers use this skill to turn selected Python, JavaScript, TypeScript, or Go code into API documentation, especially OpenAPI/Swagger-style endpoint descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms such as OpenAPI and Swagger may activate the skill when a user only mentions API documentation concepts.

Mitigation: Review routing behavior before deployment when precise activation matters.

Risk: Generated API documentation may be incomplete or inaccurate if code signatures lack sufficient context.

Mitigation: Have a developer review generated OpenAPI/Swagger output against the source code before publication or integration.

## Reference(s):

- [API Doc Generator on ClawHub](https://clawhub.ai/honestqiao/skills/api-doc-generator)

## Skill Output:

**Output Type(s):** [markdown, code, configuration, guidance]

**Output Format:** [OpenAPI/Swagger JSON or Markdown containing OpenAPI/Swagger examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated endpoint paths, summaries, parameters, response objects, and schema-like documentation derived from user-provided code.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
