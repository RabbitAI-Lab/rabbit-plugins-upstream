## Description: <br>
API 探针 helps developers and API testers generate and run REST, GraphQL, and WebSocket tests, validate API contracts, create mock services, and produce API test reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and API testers use this skill to plan API test coverage, generate test code from API definitions, validate contracts, create mock services, and summarize API test results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated tests may send POST, PUT, DELETE, load, or security-test traffic to user-supplied APIs. <br>
Mitigation: Confirm the user is authorized to test the target API, prefer staging or isolated environments, and review mutating or high-volume workflows before execution. <br>
Risk: Load and security tests can disrupt production services or trigger unintended side effects. <br>
Mitigation: Set explicit scope, rate limits, and test windows before running these tests, and avoid production unless the user has approved that environment. <br>
Risk: Imported cURL or Postman workflows may contain real credentials or production endpoints. <br>
Mitigation: Replace sample or imported secrets with test-only credentials and review endpoints before generating or running tests. <br>


## Reference(s): <br>
- [API 探针 on ClawHub](https://clawhub.ai/shylamb-token/skills/api-probe) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, generated test examples, mock service snippets, and structured report content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include mutating, load, or security-test workflows that require authorization and target-environment review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
