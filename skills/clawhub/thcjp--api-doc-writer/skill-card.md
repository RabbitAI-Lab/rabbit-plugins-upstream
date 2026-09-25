## Description:

API文档一键生成规范器 helps developers produce REST API documentation, interface specifications, RESTful design guidance, status-code guidance, and API security recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT

## Use Case:

Developers and API teams use this skill to create or standardize Markdown REST API documentation for new interfaces, review workflows, and multi-module project documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the skill as suspicious because it requests command execution authority that is not clearly needed or bounded for API documentation work.

Mitigation: Review the skill before installation in command-sensitive environments and restrict command execution to explicit, approved, documented use.

Risk: Generated API documentation can include incorrect endpoint details, authentication assumptions, status codes, or security guidance if the input API information is incomplete.

Mitigation: Have the responsible API owner review generated documentation against the implemented service before publishing or using it for integrations.

Risk: Callback URLs and API key setup guidance can expose integration metadata or credentials if handled carelessly.

Mitigation: Use trusted callback endpoints, avoid hardcoded secrets, keep credentials in environment variables or secret stores, and redact sensitive values from generated examples.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, JSON examples, shell snippets, and structured API documentation sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include REST API templates, compliance notes, changelog tables, error-handling guidance, and security recommendations.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
