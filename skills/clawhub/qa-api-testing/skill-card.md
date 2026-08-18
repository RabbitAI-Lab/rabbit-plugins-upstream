## Description:

This skill helps agents design API testing plans for RESTful, GraphQL, gRPC, and WebSocket interfaces, covering functional checks, parameter combinations, authentication and authorization checks, timeout and retry behavior, idempotency, contract validation, compatibility, and tool selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to turn API documentation and automation architecture into API test matrices, contract assertions, mock strategies, security checklists, and automation script designs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose Bash commands or live API requests while helping design or execute API testing workflows.

Mitigation: Review commands before execution, run tests only against APIs you are authorized to test, and prefer non-production environments for disruptive checks.

Risk: API security, failure, and performance testing can expose sensitive request or response data or affect service availability if run without controls.

Mitigation: Sanitize captured traffic, protect credentials and tokens, define rate and concurrency limits, and scope tests to approved systems before execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured test matrices, checklists, and optional code or command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API test plans, test cases, mock strategies, automation script designs, security checklists, compatibility impact analysis, and version migration guidance.]

## Skill Version(s):

1.7.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
