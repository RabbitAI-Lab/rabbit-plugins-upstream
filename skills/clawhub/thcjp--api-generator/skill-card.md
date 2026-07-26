## Description: <br>
Api Generator helps agents generate API scaffolding, including Express.js REST CRUD routes, GraphQL schemas, OpenAPI 3.0 documents, Python API clients, mock API servers, authentication code, rate limiters, and Jest/Supertest tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to draft backend API scaffolding and related support code for new services. It is most useful as a starting point for REST, GraphQL, OpenAPI, client, mock server, authentication, rate limiting, and API test artifacts that a developer will review before integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact documents bash command usage but does not include the referenced generator script. <br>
Mitigation: Before running any suggested bash command, confirm the actual script path and inspect the script contents. <br>
Risk: Generated API, authentication, rate limiting, and test scaffolding may not match a production service's security, persistence, or dependency requirements. <br>
Mitigation: Review, test, and adapt generated code before integrating it into a project. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/api-generator) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with code blocks and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated code is intended for stdout or redirection into project files and should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
