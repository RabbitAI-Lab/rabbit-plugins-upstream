## Description:

Validates LLM-generated JSON against required fields, types, and allowed values before downstream use, with actionable failure guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to check model-generated JSON or tool arguments against a local schema before sending them to APIs, databases, or forms, and to obtain field-level repair hints when validation fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation overstates permissions and automatic repair capabilities.

Mitigation: Treat this as a local validation helper, review its behavior before use, and handle repairs separately.

Risk: Passing unintended files may expose their contents to local validation output.

Mitigation: Provide only schema and input files intended for the tool to read.

## Reference(s):

- [Output Schema Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/output-schema-guard)
- [LGD theory background](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports field-level issues and repair hints; CLI messages default to Chinese; does not automatically repair input.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release; skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
