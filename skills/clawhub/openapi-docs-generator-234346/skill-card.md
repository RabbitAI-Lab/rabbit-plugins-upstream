## Description: <br>
Helps API developers and backend/platform teams generate, improve, and validate OpenAPI or Swagger documentation for REST APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
API developers, backend teams, developer-experience teams, and maintainers use this skill to turn REST API documentation needs into actionable OpenAPI or Swagger artifacts, checklists, implementation steps, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for broad API-documentation-related prompts because implicit invocation is enabled and trigger terms are general. <br>
Mitigation: Use explicit skill invocation when predictable routing is needed. <br>
Risk: Generated OpenAPI or Swagger guidance can be incomplete if endpoint behavior, schemas, authentication, or error cases are missing from the user's inputs. <br>
Mitigation: Review generated documentation against the service implementation and run OpenAPI validation or contract tests before publishing. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's API context and should make assumptions, limits, and verification steps visible.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
