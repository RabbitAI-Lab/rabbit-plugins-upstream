## Description:

Helps API developers, backend teams, developer-experience teams, and maintainers generate, improve, and validate OpenAPI or Swagger documentation for REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to turn REST API implementation details or existing Swagger/OpenAPI material into clearer documentation, checklists, validation steps, code snippets, and decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Implicit invocation could trigger the skill in conversations where OpenAPI documentation help was not intended.

Mitigation: Review and, if needed, narrow activation phrases or disable implicit invocation for environments where accidental invocation would be disruptive.

Risk: Generated API documentation may omit constraints or misstate endpoint behavior if source inputs are incomplete.

Mitigation: Validate generated documentation against implementation details, example requests, schema validation, and stakeholder review before publishing.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [OpenAPI RESTful API Design Article](https://blog.csdn.net/2501_94476825/article/details/159013081?ops_request_misc=elastic_search_misc&request_id=bbdb6a739ead4f3b9400c0b273e0176c&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-5-159013081-null-null.142^v102^control&utm_term=OpenAPI%20%E6%96%87%E6%A1%A3)
- [Add a Neon-authenticated public REST API and Scalar documentation](https://github.com/cuevaio/normal/issues/76)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with optional code, configuration, checklist, and shell-command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, validation steps, and remaining risks when relevant.]

## Skill Version(s):

0.20260819.45504 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
