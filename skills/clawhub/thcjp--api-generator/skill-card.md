## Description: <br>
Generates API scaffolding for RESTful Express.js CRUD endpoints, GraphQL schemas, OpenAPI 3.0 documents, Python API clients, mock servers, authentication, rate limiting, and tests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to quickly produce starting points for API services, documentation, clients, mocks, authentication helpers, rate limiters, and test suites. It is intended for API scaffold generation that is reviewed and integrated into an existing project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated authentication, authorization, and rate-limit code may be incomplete or unsuitable for a production API without project-specific review. <br>
Mitigation: Review generated security-sensitive code, test expected failure paths, and adapt it to the application's threat model before deployment. <br>
Risk: Prompts or generated files could expose real API keys, tokens, or other secrets if users include them in requests or examples. <br>
Mitigation: Use placeholders in prompts, keep secrets in environment variables or secret managers, and scan generated files before committing them. <br>
Risk: Generated scaffolds may rely on framework assumptions such as Express.js, Jest, Supertest, in-memory mocks, or Bash commands that do not match the target project. <br>
Mitigation: Validate dependencies, runtime environment, and framework conventions before copying generated output into a repository. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/api-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and code snippets, with shell commands and configuration guidance where relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated code is emitted for review and integration; production use requires developer validation of security, dependencies, and project fit.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
