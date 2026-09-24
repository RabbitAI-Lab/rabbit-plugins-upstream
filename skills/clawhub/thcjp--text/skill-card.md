## Description:

用模式转换 helps agents transform, format, clean, localize, cite, and draft text for writing and automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, independent developers, and enterprise teams use this skill to generate marketing copy, writing content, optimized titles, and structured text transformations for automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file-write and command-execution capability that is not tightly scoped to text transformation.

Mitigation: Run it only in a constrained workspace and review proposed commands or file changes before allowing execution.

Risk: Sensitive documents or API keys could be exposed if provided to a workflow whose external-service behavior is not clarified by the publisher.

Mitigation: Avoid supplying sensitive documents, secrets, or API keys unless the publisher documents exactly what is sent to external services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/text)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, text, and JSON-like structured results depending on the requested transformation mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include processed content, status metadata, command guidance, or file changes proposed by the agent.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
