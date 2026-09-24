## Description:

Formats, validates, compresses JSON data, and extracts JSONPath paths with error locations, type inference, and structural metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and automation users use this skill to inspect API responses, validate JSON syntax, compress configuration payloads, and extract field paths for mapping or debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that the skill requests or describes broader command, write, API, and credential-related capabilities than a JSON formatting task normally needs.

Mitigation: Review permissions before installation, limit the skill to the minimum required local parsing workflow when possible, and run it in a sandboxed agent environment.

Risk: The security evidence advises caution when using the skill with secrets or private JSON.

Mitigation: Use non-sensitive inputs, redact secrets before formatting or validation, and prefer a strictly local JSON formatter for private payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-formatter)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON objects and formatted text snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include formatted or compressed JSON, validation status, error details, JSONPath path lists, size metrics, depth, and key counts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
